function Settings() {

    return (

        <div style={{ padding: "20px" }}>

            <h2>⚙ AlertifyOps Settings</h2>

            <br />

            <table
                border="1"
                cellPadding="12"
                style={{
                    width: "100%",
                    borderCollapse: "collapse"
                }}
            >

                <thead>

                    <tr>

                        <th>Configuration</th>
                        <th>Current Value</th>

                    </tr>

                </thead>

                <tbody>

                    <tr>
                        <td>Duplicate Detection</td>
                        <td>Enabled</td>
                    </tr>

                    <tr>
                        <td>Reachability Check</td>
                        <td>Enabled</td>
                    </tr>

                    <tr>
                        <td>Maintenance Window Validation</td>
                        <td>Enabled</td>
                    </tr>

                    <tr>
                        <td>Auto Recovery Detection</td>
                        <td>Enabled</td>
                    </tr>

                    <tr>
                        <td>Historical Correlation</td>
                        <td>Enabled</td>
                    </tr>

                    <tr>
                        <td>AI Root Cause Analysis</td>
                        <td>Enabled</td>
                    </tr>

                    <tr>
                        <td>Confidence Threshold</td>
                        <td>90%</td>
                    </tr>

                    <tr>
                        <td>ServiceNow Integration</td>
                        <td>Connected</td>
                    </tr>

                    <tr>
                        <td>SolarWinds Integration</td>
                        <td>Connected</td>
                    </tr>

                </tbody>

            </table>

        </div>

    );

}

export default Settings;