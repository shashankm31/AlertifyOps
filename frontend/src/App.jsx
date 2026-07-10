import DashboardCards from "./components/DashboardCards";
import Navbar from "./components/Navbar";
import AlertsTable from "./components/AlertsTable";
import Sidebar from "./components/Sidebar";



function App() {
  return (

    <div style = {{ display: "flex" }}>

      <Sidebar />

      <div style = {{ flex: 1 }}>  

         <Navbar />

         <DashboardCards />
         
         <AlertsTable />

         </div>
         </div>
  );
}


export default App;