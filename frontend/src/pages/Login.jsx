import { useState } from 'react';

function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        const response = await fetch("http://localhost:8000/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
            username: email,
            password: password,
        }),
    });

    const data = await response.json();

    localStorage.setItem("access_token", data.access_token);

    console.log(data);
};


    return (
        <div>
            <h1>Login</h1>

            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />

            <br />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <br />

            <button onClick={handleLogin}>Login</button>
            </div>
    );
}

export default Login;