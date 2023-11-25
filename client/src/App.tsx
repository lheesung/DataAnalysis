import React, { useState, useEffect, ChangeEvent } from "react";
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

interface DataItem {
  Date: string;
  Value: number;
}

interface CountryItem {
  name: string;
}

function App() {
  const [data, setData] = useState<DataItem[]>([]);
  const [countries, setCountries] = useState<CountryItem[]>([]);
  const [country, setCountry] = useState<string>("World");
  const [indicator, setIndicator] = useState<string>("temperature");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/countries")
      .then((response) => {
        setCountries(response.data);
      })
      .catch((error) => console.error("Error fetching countries: ", error));

    axios
      .get(
        `http://127.0.0.1:5000/data?country=${country}&indicator=${indicator}`
      )
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data: ", error);
      });
  }, [country, indicator]);

  const handleCountryChange = (e: ChangeEvent<HTMLSelectElement>) => {
    setCountry(e.target.value);
  };

  const handleIndicatorChange = (e: ChangeEvent<HTMLSelectElement>) => {
    setIndicator(e.target.value);
  };

  return (
    <div>
      <select value={country} onChange={handleCountryChange}>
        {countries &&
          countries.map((countryItem) => (
            <option key={countryItem.name} value={countryItem.name}>
              {countryItem.name}
            </option>
          ))}
      </select>
      <select value={indicator} onChange={handleIndicatorChange}>
        <option value="temperature">연도별 온도 변화</option>
        <option value="co2">대기 중 CO2 농도</option>
        <option value="sea_level">해수면 변화 값</option>
      </select>
      <LineChart width={600} height={300} data={data}>
        <XAxis dataKey="Date" />
        <YAxis />
        <CartesianGrid strokeDasharray="3 3" />
        <Tooltip />
        <Legend />
        <Line
          type="monotone"
          dataKey="Value"
          stroke="#8884d8"
          activeDot={{ r: 8 }}
        />
      </LineChart>
    </div>
  );
}

export default App;
