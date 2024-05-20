import React, { useEffect, useState } from 'react';

const App: React.FC = () => {
  const [message, setMessage] = useState<string>('');
  const [error, setError] = useState<string>('');

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/hello')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => setMessage(data.message))
      .catch(error => setError(error.message));
  }, []);

  return (
    <div>
      <h1>{message}</h1>
      {error && <p>Error: {error}</p>}
    </div>
  );
}

export default App;
