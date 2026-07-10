function DashboardCards() {
    return (
        <div
          style = {{
            display: "flex",
            gap: "20px",
            padding: "20px",
          }}
        >
            <div style = {cardStyle}>
                <h3> Total Alerts </h3>
                <h1> 125 </h1>
            </div>

            <div style = {cardStyle}>
                <h3> critical Alerts </h3>
                <h1> 12 </h1>
            </div>

            <div style = {cardStyle}>
                <h3> Warning Alerts </h3>
                <h1> 38 </h1>
            </div>

            <div style = {cardStyle}>
                <h3> Healthy Devices </h3>
                <h1> 245 </h1>
            </div>
            </div>
    );
}

const cardStyle = {
    backgroundColor: "white",
    padding: "20px",
    borderRadius: "10px",
    boxShadow: "0px 2px 8px rgba(0,0,0,0.2)",
    width: "220px",
    textAlign: "center",
};

export default DashboardCards;
        