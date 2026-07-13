import { Link } from "react-router-dom";


function Sidebar() {
    const linkStyle = {
        color: "white",
        textDecoration: "none",
        display: "block",
        padding: "10px 0px",
        frontSize: "18px",
    };
    
    return (
      <div
        style = {{
          width: "240px",
          backgroundColor: "#1E1E2F",
          color: "white",
          minHeight: "100vh",
          padding: "20px",
        }}
    >
            <h2>🚨 AlertifyOps </h2>

            <hr style={{ marginBottom: "20px" }} />
            
            <Link to = "/" style = {linkStyle}>
                🏠 Dashboard   
            </Link>

            <Link to = "/incoming-alerts" style = {linkStyle}>
                📡 Incoming Alerts 
            </Link>

            <Link to = "/validated-alerts" style = {linkStyle}>
                ✅ Validated Alerts
            </Link>

            <Link to = "/suppressed-alerts" style = {linkStyle}>
                🚫 Suppressed Alerts
            </Link>

            <Link to = "/incidents" style = {linkStyle}>
                🎫 Incidents
            </Link>

            <Link to = "/ai-insights" style = {linkStyle}>
                🤖 AI Insights
            </Link>

            <Link to = "/mttr-analytics" style = {linkStyle}>
                📊 MTTR Analytics
            </Link>

            <Link to = "/settings" style = {linkStyle}>
                ⚙ Settings
            </Link>
          </div>
    );
  }

  export default Sidebar;
