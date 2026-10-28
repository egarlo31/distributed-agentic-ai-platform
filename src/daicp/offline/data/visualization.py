"""Build offline audit figures and dashboards from previously inspected data."""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class DataVisualization:
    """Render Plotly views of source inventories, quality and operational coverage."""


    @staticmethod
    def plot_file_distribution(inventory: pd.DataFrame) -> go.Figure:
        """Visualize file counts and storage distribution by format."""

        summary = (
            inventory.groupby("extension", as_index=False)
            .agg(
                files=("extension", "count"),
                size_mb=("size_bytes", lambda x: x.sum() / 1024**2)
            )
            .sort_values("size_mb", ascending=False)
        )

        fig = px.bar(
            summary,
            x="extension",
            y="size_mb",
            text="files",
            title="File Distribution by Format",
            labels={
                "extension": "File Format",
                "size_mb": "Storage (MiB)",
                "files": "File Count"
            },
            template="plotly_white"
        )

        fig.update_traces(textposition="outside")
        fig.update_layout(showlegend=False)

        return fig

    @staticmethod
    def plot_category_frequency(df: pd.DataFrame, column: str, title: str) -> go.Figure:
        """Visualize category frequencies, including list-valued categories."""

        counts = df.explode(column)[column].value_counts().reset_index()
        counts.columns = [column, "count"]

        fig = px.bar(
            counts,
            x="count",
            y=column,
            orientation="h",
            text="count",
            title=title,
            labels={"count": "Frequency", column: "Category"},
            template="plotly_white"
        )

        fig.update_layout(
            yaxis={"categoryorder": "total ascending"},
            showlegend=False
        )

        return fig

    @staticmethod
    def plot_numeric_by_category(df: pd.DataFrame, category: str, value: str, title: str) -> go.Figure:
        """Compare numeric distributions across categories."""

        fig = px.box(
            df,
            x=value,
            y=category,
            orientation="h",
            points="outliers",
            title=title,
            template="plotly_white"
        )

        fig.update_layout(
            xaxis_title=value.replace("_", " ").title(),
            yaxis_title=category.replace("_", " ").title()
        )

        return fig

    @staticmethod
    def plot_percentage_by_category(df: pd.DataFrame, category: str, value: str, title: str) -> go.Figure:
        """Visualize percentages across categories."""

        fig = px.bar(
            df.sort_values(value),
            x=value,
            y=category,
            orientation="h",
            text=value,
            title=title,
            template="plotly_white"
        )

        fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig.update_layout(
            height=max(450, 30 * len(df)),
            showlegend=False,
            xaxis_title="Percentage (%)"
        )

        return fig

    @staticmethod
    def plot_audit_dashboard(faults: pd.DataFrame, logs: pd.DataFrame, availability: pd.DataFrame,
                             consistency: pd.DataFrame) -> go.Figure:
        """Generate the SRC-002 audit dashboard."""

        fig = make_subplots(
            rows=3,
            cols=2,
            subplot_titles=[
                "Fault Type Distribution",
                "Most Targeted Network Functions",
                "Fault Duration Distribution",
                "Log Warning/Error Rate",
                "Network Function DOWN Rate",
                "Operational Evidence Coverage"
            ],
            vertical_spacing=0.12,
            horizontal_spacing=0.16
        )

        # 1. Fault types
        counts = faults["fault_type"].value_counts()
        fig.add_trace(
            go.Bar(x=counts.index, y=counts.values, text=counts.values),
            row=1, col=1
        )

        # 2. Target network functions
        targets = faults.explode("targets")["targets"].value_counts().head(10)
        fig.add_trace(
            go.Bar(x=targets.values[::-1], y=targets.index[::-1], orientation="h"),
            row=1, col=2
        )

        # 3. Fault durations
        fig.add_trace(
            go.Histogram(x=faults["duration_sec"], nbinsx=20),
            row=2, col=1
        )

        # 4. Log severity
        log_summary = logs.nlargest(10, "events").sort_values("warning_error_pct")
        fig.add_trace(
            go.Bar(
                x=log_summary["warning_error_pct"],
                y=log_summary["nf"],
                orientation="h"
            ),
            row=2, col=2
        )

        # 5. NF availability
        nf_summary = availability.nlargest(10, "down_pct").sort_values("down_pct")
        fig.add_trace(
            go.Bar(
                x=nf_summary["down_pct"],
                y=nf_summary["nf"],
                orientation="h"
            ),
            row=3, col=1
        )

        # 6. Evidence coverage
        coverage = {
            "Fault Windows": int(consistency["label_window_match"].sum()),
            "Target Logs": int(consistency["log_events"].gt(0).sum()),
            "Global Matrix": int(consistency["global_observations"].gt(0).sum()),
            "NF Metrics": int(consistency["metric_samples"].gt(0).sum()),
            "Successful Scrapes": int(consistency["successful_scrapes"].gt(0).sum())
        }

        fig.add_trace(
            go.Bar(
                x=list(coverage.values()),
                y=list(coverage.keys()),
                orientation="h",
                text=list(coverage.values())
            ),
            row=3, col=2
        )

        fig.update_layout(
            title=f"SRC-002 CoreOps | Data Audit Dashboard — {len(faults)} Incidents",
            template="plotly_white",
            height=1350,
            showlegend=False,
            margin=dict(t=110, b=70, l=100, r=50)
        )

        fig.update_xaxes(tickangle=-35, row=1, col=1)
        fig.update_xaxes(title_text="Duration (seconds)", row=2, col=1)
        fig.update_xaxes(title_text="Warning/Error (%)", row=2, col=2)
        fig.update_xaxes(title_text="DOWN observations (%)", row=3, col=1)
        fig.update_xaxes(title_text="Incidents", range=[0, len(faults)], row=3, col=2)

        return fig