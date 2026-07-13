import { Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";

import Dashboard from "./pages/Dashboard";
import IncomingAlerts from "./pages/IncomingAlerts";
import ValidatedAlerts from "./pages/ValidatedAlerts";
import SuppressedAlerts from "./pages/SuppressedAlerts";
import Incidents from "./pages/Incidents";
import AIInsights from "./pages/AIInsights";
import MTTRAnalytics from "./pages/MTTRAnalytics";
import Settings from "./pages/Settings";


function App() {
  return (

    <div style = {{ display: "flex" }}>
      <Sidebar />

      <div style = {{ flex: 1 }}>  
         <Navbar />

        <Routes>
          <Route path = "/" 
           element = {<Dashboard />} 
           />

          <Route 
           path = "/incoming-alerts" 
           element = {<IncomingAlerts />} 
           />

          <Route 
           path = "/validated-alerts" 
           element = {<ValidatedAlerts />} 
           />

          <Route 
           path = "/suppressed-alerts" 
           element = {<SuppressedAlerts />} 
           />

          <Route 
           path = "/incidents" 
           element = {<Incidents />} 
           />

          <Route 
           path = "/ai-insights" 
           element = {<AIInsights />} 
           />

          <Route 
           path = "/mttr-analytics" 
           element = {<MTTRAnalytics />} 
           />

          <Route 
           path = "/settings" 
           element = {<Settings />} 
           />
        

        </Routes>
      </div>
    </div>
  );
}


export default App;