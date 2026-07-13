function AIInsights() {

    const insights = [

        {
            alert: "Node Down",
            confidence: "96%",
            cause: "WAN Link Failure",
            recommendation: "Check ISP circuit and BGP session."
        },

        {
            alert: "CPU High",
            confidence: "91%",
            cause: "Application consuming CPU",
            recommendation: "Restart application service."
        },

        {
            alert: "Interface Down",
            confidence: "89%",
            cause: "Possible Fiber Cut",
            recommendation: "Verify optical power and SFP."
        }

    ];

    return (

        <div style={{ padding: "20px" }}>

            <h2>🤖 AI Root Cause Insights</h2>

            <br />

            {

                insights.map((item,index)=>(

                    <div
                        key={index}
                        style={{
                            border:"1px solid #ddd",
                            borderRadius:"10px",
                            padding:"20px",
                            marginBottom:"20px",
                            boxShadow:"0 2px 8px rgba(0,0,0,0.1)"
                        }}
                    >

                        <h3>{item.alert}</h3>

                        <p><b>AI Confidence:</b> {item.confidence}</p>

                        <p><b>Predicted Root Cause:</b> {item.cause}</p>

                        <p><b>Recommendation:</b> {item.recommendation}</p>

                    </div>

                ))

            }

        </div>

    );

}

export default AIInsights;