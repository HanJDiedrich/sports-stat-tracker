import React, { useRef, useState, useEffect } from 'react';

const BasketballCourt = () => {
  const canvasRef = useRef(null);
  const [shots, setShots] = useState([]);

  // Draw basketball court background image when the component mounts
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const image = new Image();
    image.src = '/court.jpg'; // Replace with your court image path
    image.onload = () => {
      ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
    };
  }, []);

  // Handle click events to log shot coordinates and type
  const handleClick = (e) => {
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();

    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const shotType = isThreePointShot(x, y) ? '3PT' : '2PT';
    console.log(`Shot recorded at: (${x}, ${y}) - ${shotType}`);

    setShots([...shots, { x, y, type: shotType }]);
  };

  // Function to determine if the shot is a 3-pointer based on coordinates
  const isThreePointShot = (x, y) => {
    const courtWidth = 800; // Canvas width
    const courtHeight = 450; // Canvas height

    const threePointRadius = 200; // Adjust this radius to match your court
    const centerX = courtWidth / 2;
    const centerY = courtHeight;

    const distance = Math.sqrt((x - centerX) ** 2 + (y - centerY) ** 2);
    return distance > threePointRadius;
  };

  return (
    <div>
      <canvas
        ref={canvasRef}
        width={800}
        height={450}
        onClick={handleClick}
        style={{ border: '1px solid black' }}
      />
      <div>
        <h3>Shot Log</h3>
        <ul>
          {shots.map((shot, index) => (
            <li key={index}>
              {shot.type} shot at ({shot.x}, {shot.y})
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default BasketballCourt;
