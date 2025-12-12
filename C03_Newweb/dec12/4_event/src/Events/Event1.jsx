const Event1 = () => {
    const testmessage = (e) => {
        alert(e.target);
        alert(e.target.value);
        alert(e.target.name);
    };
    return (
        <input
            name="abc"
            onClick={(e) => {
                alert("클릭 감지");
            }}
            onChange={testmessage}
        />
    );
};

export default Event1;
