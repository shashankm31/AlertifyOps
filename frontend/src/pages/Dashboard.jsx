import DashboardCards from "../components/DashboardCards";
import AlertsTable from "../components/AlertsTable";


function Dashboard() {
    return (
        <div>
            <h2>Dashboard</h2>
            <DashboardCards />
            <AlertsTable />
        </div>
    );
}

export default Dashboard;