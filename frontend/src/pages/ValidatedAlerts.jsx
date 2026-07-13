import StatusBadge from "../components/StatusBadge";

function ValidatedAlerts() {

    const validations = [

        {
            device: "RTR-01",
            alert: "Node Down",
            duplicate: "No",
            reachable: "No",
            maintenance: "No",
            recovered: "No",
            decision: "Create Incident"
        },

        {
            device: "SW-02",
            alert: "Interface Down",
            duplicate: "Yes",
            reachable: "Yes",
            maintenance: "No",
            recovered: "Yes",
            decision: "Suppress"
        }

    ];

    return (

        <div style={{ padding: "20px" }}>

            <h2>Validated Alerts</h2>

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
                        <th>Duplicate</th>
                        <th>Reachable</th>
                        <th>Maintenance</th>
                        <th>Recovered</th>
                        <th>Decision</th>

                    </tr>

                </thead>

                <tbody>

                    {validations.map((item,index)=>(

                        <tr key={index}>

                            <td>{item.device}</td>

                            <td>{item.alert}</td>

                            <td>{item.duplicate}</td>

                            <td>{item.reachable}</td>

                            <td>{item.maintenance}</td>

                            <td>{item.recovered}</td>

                            <td>

                                <StatusBadge status={item.decision} />

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default ValidatedAlerts;
  