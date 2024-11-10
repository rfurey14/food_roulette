// List of 20 countries
const countries = [
    "USA", "Canada", "Brazil", "China", "India", "Russia", "Australia", "Germany", 
    "France", "Italy", "Japan", "South Korea", "Mexico", "Argentina", "Egypt", 
    "Nigeria", "South Africa", "Saudi Arabia", "Turkey", "United Kingdom", "Spain"
];

// Function to select and display a random country
function spin() {
    const countryName = document.getElementById("country-name");

    // Start the "flicker" effect by changing the country names multiple times
    let flickerCount = 10;  // Number of flickers before settling on the final country
    const flickerInterval = setInterval(() => {
        const randomIndex = Math.floor(Math.random() * countries.length);
        countryName.textContent = countries[randomIndex];
    }, 100);  // Change country text every 100ms

    // After the flickering, show the final country after a short delay
    setTimeout(() => {
        const randomIndex = Math.floor(Math.random() * countries.length);
        countryName.textContent = countries[randomIndex];
        clearInterval(flickerInterval);  // Stop the flicker effect
    }, flickerCount * 100);  // The flicker interval duration
}









  
  
  
  