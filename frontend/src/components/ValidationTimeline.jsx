function ValidationTimeline() {

    const steps = [
        "Incoming Alert",
        "Duplicate Check",
        "Maintenance Window",
        "Reachability Test",
        "Historical Pattern",
        "Incident Created",
    ];

    return (

        <div style = {{ padding: "20px" }}>

            <h3> Validation Timeline</h3>

            {steps.map((step, index) => (

                <div
                    key = {index}
                    style = {{
                        display: "flex",
                        alignItems: "center",
                        marginBottom: "15px"
                    }}
                >
                    <div
                        style = {{
                            width: "20px",
                            height: "18px",
                            borderRadius: "50%",
                            backgroundColor: "#22c55e",
                            marginRight: "15px"
                        }}
                    />

                    <span>{step}</span>

                </div>

                    ))}
        </div>
    );

}

export default ValidationTimeline;