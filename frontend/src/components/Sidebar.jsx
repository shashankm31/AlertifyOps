function Sidebar() {
    return (
        <div
          style={{
            width: "240px",
            backgroundColor: "#111827",
            color: "white",
            minHeight: "100vh",
            padding: "20px",
          }}
          >
            <h2> AlertifyOps </h2>

            <hr />

            <p> Dashboard </p>
            <p> incoming Alerts </p>
            <p> Validated Alerts </p>
            <p> Suppressed Alerts </p>
            <p> incidents </p>
            <p> AI Insights </p>
            <p> MTTR Analytics </p>
            <p> Settings </p>

          </div>
    );
  }

  export default Sidebar;
