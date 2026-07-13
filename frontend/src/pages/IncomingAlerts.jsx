import StatusBadge from "../components/StatusBadge";
import ValidationTimeline from "../components/ValidationTimeline";

function IncomingAlerts() {

    const alerts = [

        {
            device: "RTR-01",
            alert: "Node Down",
            severity: "Critical",
            time: "10:22",
            status: "New"
        },

        {
            device: "SW-02",
            alert: "Interface Down",
            severity: "Warning",
            time: "10:25",
            status: "Pending"
        },

        {
            device: "FW-01",
            alert: "CPU High",
            severity: "Critical",
            time: "10:30",
            status: "Pending"
        }

        

    ];

    return (

        <div style = {{ padding: "20px" }}>

            <h2>Incoming Alerts</h2>

            <br />

            <input
                type = "text"
                placeholder = "Search alerts..."
                style = {{ 
                    padding: "10px",
                    width: "300px",
                }}
            /> 

            <br /><br />

            <table 
                border = "1"
                cellPadding = "12"
                style = {{
                    borderCollapse: "collapse",
                    width: "100%"
                }}
            >
                <thead>

                    <tr>

                        <th>Device</th>
                        <th>alert</th>
                        <th>Severity</th>
                        <th>Time</th>
                        <th>Status</th>

                    </tr>

                </thead>

                <tbody>

                    {alerts.map((item,index) => (

                        <tr key = {index}>

                            <td>{item.device}</td>
                            <td>{item.alert}</td>
                            <td><StatusBadge status={item.severity} /></td>
                            <td>{item.time}</td>
                            <td><StatusBadge status={item.status} /></td>

                        </tr>

                    ))}

                </tbody>

            </table>

            <hr />

            <ValidationTimeline />

        </div>

    );
          
}

export default IncomingAlerts;