import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function FormPage() {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    sex: '',
    height: '',
    currentWeight: '',
    targetWeight: '',
  });

  const navigate = useNavigate();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    fetch("http://127.0.0.1:5000/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
    .then((res) => res.json())
    .then((data) => {
      localStorage.setItem("fitnessResponse", JSON.stringify(data));
      navigate("/results");
    })
    .catch((error) => console.error("Error sending data to API:", error));
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Enter Your Fitness Details</h1>
        <form onSubmit={handleSubmit}>
          <input type="text" name="name" placeholder="Name" value={formData.name} onChange={handleChange} required />
          <input type="number" name="age" placeholder="Age" value={formData.age} onChange={handleChange} required />
          <select name="sex" value={formData.sex} onChange={handleChange} required>
            <option value="">Select Sex</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
          </select>
          <input type="number" name="height" placeholder="Height (cm)" value={formData.height} onChange={handleChange} required />
          <input type="number" name="currentWeight" placeholder="Current Weight (kg)" value={formData.currentWeight} onChange={handleChange} required />
          <input type="number" name="targetWeight" placeholder="Target Weight (kg)" value={formData.targetWeight} onChange={handleChange} required />
          <button type="submit">Submit</button>
        </form>
      </header>
    </div>
  );
}

export default FormPage;