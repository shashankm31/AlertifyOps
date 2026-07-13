import StatusBadge from "../components/StatusBadge";

function SuppressedAlerts() {

    const alerts = [

        {
            device: "SW-02",
            alert: "Interface Down",
            reason: "Duplicate Alert",
            action: "Suppressed"
        },

        {
            device: "RTR-03",
            alert: "Node Down",
            reason: "Maintenance Window",
            action: "Suppressed"
        },

        {
            device: "FW-01",
            alert: "CPU High",
            reason: "Auto Recovered",
            action: "Suppressed"
        },

        {
            device: "RTR-04",
            alert: "BGP Down",
            reason: "Alert Flapping",
            action: "Suppressed"
        }

    ];

    return (

        <div style={{ padding: "20px" }}>

            <h2>Suppressed Alerts</h2>

            <br />

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

                        <th>Device</th>
                        <th>Alert</th>
                        <th>Reason</th>
                        <th>Status</th>

                    </tr>

                </thead>

                <tbody>

                    {alerts.map((item,index)=>(

                        <tr key={index}>

                            <td>{item.device}</td>

                            <td>{item.alert}</td>

                            <td>{item.reason}</td>

                            <td>

                                <StatusBadge status={item.action} />

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default SuppressedAlerts;