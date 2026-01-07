import { Route, Routes } from "react-router-dom";
import "./App.css";
import Home from "./msAISA/layout/content/home/home";
import MemberInfo from "./msAISA/layout/content/member/memberInfo";
import SignUpForm from "./msAISA/layout/content/member/signUpForm";
import SNS from "./msAISA/layout/content/sns/sns";
import MSAISAMain from "./msAISA/msAISAMain";

function App() {
   return (
      <Routes>
         <Route element={<MSAISAMain />}>
            <Route index element={<Home />} />
            <Route path="/sign.up.go" element={<SignUpForm />} />
            <Route path="/member.info.go" element={<MemberInfo />} />
            <Route path="/sns.go" element={<SNS />} />
         </Route>
      </Routes>
   );
}

export default App;
