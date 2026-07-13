function MTTRAnalytics() {

    const metrics = [

        {
            title: "Average MTTR",
            value: "8 min"
        },

        {
            title: "Alert Noise Reduced",
            value: "62%"
        },

        {
            title: "Incidents Prevented",
            value: "145"
        },

        {
            title: "Validation Accuracy",
            value: "97%"
        }

    ];

    return (

        <div style={{ padding: "20px" }}>

            <h2>📊 MTTR Analytics</h2>

            <br />

            <div
                style={{
                    display: "flex",
                    gap: "20px",
                    flexWrap: "wrap"
                }}
            >

                {metrics.map((metric,index)=>(

                    <div
                        key={index}
                        style={{
                            background: "white",
                            width: "220px",
                            padding: "20px",
                            borderRadius: "10px",
                            boxShadow: "0px 2px 8px rgba(0,0,0,0.2)",
                            textAlign: "center"
                        }}
                    >

                        <h3>{metric.title}</h3>

                        <h1>{metric.value}</h1>

                    </div>

                ))}

            </div>

            <br />
            <br />

            <h3>Monthly Improvements</h3>

            <table
                border="1"
                cellPadding="10"
                style={{
                    width: "100%",
                    borderCollapse: "collapse"
                }}
            >

                <thead>

                    <tr>

                        <th>Metric</th>
                        <th>Before AlertifyOps</th>
                        <th>After AlertifyOps</th>

                    </tr>

                </thead>

                <tbody>

                    <tr>

                        <td>Average MTTR</td>
                        <td>35 min</td>
                        <td>8 min</td>

                    </tr>

                    <tr>

                        <td>False Alerts</td>
                        <td>420</td>
                        <td>150</td>

                    </tr>

                    <tr>

                        <td>Duplicate Tickets</td>
                        <td>180</td>
                        <td>12</td>

                    </tr>

                    <tr>

                        <td>Suppression Rate</td>
                        <td>0%</td>
                        <td>62%</td>

                    </tr>

                </tbody>

            </table>

        </div>

    );

}

export default MTTRAnalytics;