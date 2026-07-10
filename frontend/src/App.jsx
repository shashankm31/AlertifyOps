import DashboardCards from "./components/DashboardCards";


function App() {
  return (
    <div>
      <header
        style={{
          backgroundColor: "#1f2937",
          color: "white",
          padding: "20px",
          textAlign: "center",
        }}
        >
         <h1> AlertifyOps Dashboard </h1>
         </header>

         <DashboardCards />
         </div>
  );
}


export default App;