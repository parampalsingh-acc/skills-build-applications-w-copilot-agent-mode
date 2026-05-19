import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Fetching from:', apiUrl);
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        console.log('Fetched data:', data);
        setActivities(data.results ? data.results : data);
      })
      .catch(error => console.error('Error fetching activities:', error));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2>Activities</h2>
      <table className="table table-striped">
        <thead>
          <tr><th>ID</th><th>User</th><th>Type</th><th>Duration</th></tr>
        </thead>
        <tbody>
          {activities.map((activity, index) => (
            <tr key={index}>
              <td>{activity._id || activity.id}</td>
              <td>{activity.user}</td>
              <td>{activity.activity_type}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
