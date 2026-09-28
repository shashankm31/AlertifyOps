function AlertsTable({ alerts })
   {
    
    return (
        <div style={{ padding: "20px" }}>
            <h2> Recent Alerts </h2>

            <table
              style = {{
                width: "100%",
                borderCollapse: "collapse",
                marginTop: "15px",
                backgroundColor: "white",
                boxShadow: "0px 2px 8px rgba(0,0,0,0.2)",
              }}
              >
                <thead
                  style = {{
                    backgroundColor: "#1f2937",
                    color: "white",
                  }}
                >
                    <tr>
                        <th style = {cellStyle} > Device </th>
                        <th style = {cellStyle} > Alert </th>
                        <th style = {cellStyle} > Severity </th>
                        <th style = {cellStyle} > Status </th>
                    </tr>
                </thead>

                <tbody>
                    {alerts.map((alert) => (

                        <tr key = {alert.id}>
                            <td style = {cellStyle}>{alert.device} </td>
                            <td style = {cellStyle}>{alert.alert_type} </td>
                            <td style = {cellStyle}>{alert.severity} </td>
                            <td style = {cellStyle}>{alert.status} </td>
                        </tr>
                    ))}
                </tbody>
              </table>
              </div>
    );
}

const cellStyle = {
    border: "1px solid #ddd",
    padding: "12px",
    textAlign: "center",
};

export default AlertsTable;