import { useState, useEffect } from "react";
import styles from "../styles/Home.module.css";

import axios from "axios";

export default function Home() {
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState("");

  useEffect(() => {
    axios
      .get("/hello")
      .then((res) => {
        setMessage(res.data.message);
        setLoading(false);
      })
      .then((data) => {});
  }, []);
  return (
    <div className={styles.container}>
      <p>{!loading ? message : " Loading.."}</p>
    </div>
  );
}
