function StatusBadge({ status }) {

    let backgroundColor = "#3b82f6";

    if (status === "Critical") {
        backgroundColor = "#ef4444";
    }

    if (status === "Warning") {
        backgroundColor = "#f59e0b";
    }

    if (status === "Healthy") {
        backgroundColor = "#22c55e";
    }

    if (status === "Pending") {
        backgroundColor = "#3b82f6";
    }

    if (status === "Validated") {
        backgroundColor = "#10b981";
    }

    if (status === "Suppressed") {
        backgroundColor = "#6b7280";
    }

    if (status === "Create Incident") {
        backgroundColor = "#ef4444";
    }

    if (status === "Suppress") {
        backgroundColor = "#6b7280";
    }

    if (status === "Suppressed") {
        backgroundColor = "#6b7280";
    }

    if (status === "Open") {
        backgroundColor = "#ef4444";
    }

    if (status === "Assigned") {
        backgroundColor = "#f59e0b";
    }

    if (status === "Resolved") {
        backgroundColor = "#22c55e";
    }

    return (

        <span
            style = {{
                backgroundColor,
                color: "white",
                padding: "6px 12px",
                borderRadius: "20px",
                fontWeight: "bold",
                fontSize: "14px",
            }}
        >

            {status}
        </span>
    );

}

export default StatusBadge;