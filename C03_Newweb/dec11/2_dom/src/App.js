import "./App.css";
import Props1 from "./Props/Props1";
import Props2 from "./Props/Props2";
import Props3 from "./Props/Props3";
import Props4 from "./Props/Props4";

// Props(Properties): 여러 속성, 특성

function App() {
    // '속성'으로 데이터를 주고받는 것이 가능하다.
    return (
        <>
            <Props1 name="홍길동" age="30" />
            <Props1 name="김길동" age="20" />
            <hr />
            <hr />
            <Props2 name="초코파이" price="5000" />
            <hr />
            <hr />
            <Props3 cpu="i7 15세대" ram="32" storagetype="SSD" storagesize="2" />
            <hr />
            <hr />
            <Props3 storagetype="1231234" storagesize="!!!" />
            <hr />
            <Props4>박주현</Props4>

        </>
    ); // 막 어겨도 정상 실행된다.
}

export default App;
