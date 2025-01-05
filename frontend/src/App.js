import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [students, setStudents] = useState([]); 
  const [page, setPage] = useState(1); 
  const [pageSize, setPageSize] = useState(10); 

  useEffect(() => {
    fetch(`http://127.0.0.1:3000/students/?page=${page}&page_size=${pageSize}`)
      .then((response) => response.json())
      .then((data) => setStudents(data))
      .catch((error) => console.error("Error fetching students:", error));
  }, [page, pageSize]);

  return (
    <div className="App">
      <h1>Student Management</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Last Name</th>
            <th>First Name</th>
            <th>Middle Name</th>
            <th>Course</th>
            <th>Group Name</th>
            <th>Faculty</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => (
            <tr key={student.id}>
              <td>{student.id}</td>
              <td>{student.last_name}</td>
              <td>{student.first_name}</td>
              <td>{student.middle_name}</td>
              <td>{student.course}</td>
              <td>{student.group_name}</td>
              <td>{student.faculty}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="pagination">
        <button onClick={() => setPage(page - 1)} disabled={page === 1}>
          Previous
        </button>
        <span> Page {page} </span>
        <button onClick={() => setPage(page + 1)}>Next</button>
        <select onChange={(e) => setPageSize(Number(e.target.value))}>
          <option value="10">10</option>
          <option value="20">20</option>
          <option value="50">50</option>
        </select>
      </div>
    </div>
  );
}

export default App;
