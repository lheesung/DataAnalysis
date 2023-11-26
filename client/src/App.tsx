import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";
import * as S from "./style/style";

interface DataItem {
  Date: string;
  Value: number;
}

function App() {
  const [data, setData] = useState<DataItem[]>([]);
  const [indicator, setIndicator] = useState<string>("temperature");

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:5000/data?country=World&indicator=${indicator}`)
      .then((response) => {
        console.log("Received data:", response.data);
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [indicator]);

  return (
    <S.Container>
      <S.Title>죽어가는 지구 ㅠㅠ</S.Title>
      <select value={indicator} onChange={(e) => setIndicator(e.target.value)}>
        <option value="co2">대기 중 CO2 농도</option>
        <option value="sea_level">해수면 변화 값</option>
      </select>
      <LineChart width={1200} height={400} data={data}>
        <XAxis dataKey="Date" />
        <YAxis />
        <CartesianGrid strokeDasharray="3 3" />
        <Tooltip />
        <Line type="monotone" dataKey="Value" stroke="#8884d8" />
        <Legend />
      </LineChart>
    </S.Container>
  );
}

export default App;
