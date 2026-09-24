import DashboardCards from "../components/DashboardCards";
import AlertsTable from "../components/AlertsTable";
import { useEffect, useState } from "react";

function Dashboard() {
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {

        fetch("http://localhost:8000/alerts").then(
            response => response.json()).then(
                data => {
                    setAlerts(data);
                });
            }, []);

            console.log(alerts);

    return (
        <div>
            <h2>Dashboard</h2>
            <DashboardCards />
            <AlertsTable />
        </div>
    );
}

export default Dashboard;