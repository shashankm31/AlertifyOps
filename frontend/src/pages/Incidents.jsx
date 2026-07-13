import StatusBadge from "../components/StatusBadge";

function Incidents() {

    const incidents = [

        {
            incident: "INC0001234",
            device: "RTR-01",
            alert: "Node Down",
            priority: "P1",
            team: "Network Team",
            status: "Open"
        },

        {
            incident: "INC0001235",
            device: "FW-01",
            alert: "CPU High",
            priority: "P2",
            team: "Server Team",
            status: "Assigned"
        },

        {
            incident: "INC0001236",
            device: "RTR-10",
            alert: "BGP Down",
            priority: "P1",
            team: "Network Team",
            status: "Resolved"
        }

    ];

    return (

        <div style={{ padding: "20px" }}>

            <h2>Incidents</h2>

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

                        <th>Incident</th>
                        <th>Device</th>
                        <th>Alert</th>
                        <th>Priority</th>
                        <th>Assignment Group</th>
                        <th>Status</th>

                    </tr>

                </thead>

                <tbody>

                    {incidents.map((item,index)=>(

                        <tr key={index}>

                            <td>{item.incident}</td>

                            <td>{item.device}</td>

                            <td>{item.alert}</td>

                            <td>{item.priority}</td>

                            <td>{item.team}</td>

                            <td>

                                <StatusBadge status={item.status} />

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default Incidents;