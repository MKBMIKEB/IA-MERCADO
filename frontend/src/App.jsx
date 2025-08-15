import { useEffect } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

function App() {
  useEffect(() => {
    const map = L.map('map').setView([4.60971, -74.08175], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors',
    }).addTo(map);
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">IA Mercado</h1>
      <div id="map" className="h-64"></div>
    </div>
  );
}

export default App;
