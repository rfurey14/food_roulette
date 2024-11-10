async function fetchMeals() {
    const country = document.getElementById('country').value;
    const mealsContainer = document.getElementById('meals');
    const errorContainer = document.getElementById('error');
    
    mealsContainer.innerHTML = '';
    errorContainer.innerText = '';

    try {
        const response = await fetch(`http://127.0.0.1:5000/meals?country=${country}`);
        const data = await response.json();

        if (response.ok) {
            if (data.meal_pics) {
                Object.entries(data.meal_pics).forEach(([mealName, imageUrl]) => {
                    const mealDiv = document.createElement('div');
                    mealDiv.className = 'meal';
                    mealDiv.innerHTML = `
                        <h3>${mealName}</h3>
                        <img src="${imageUrl}" alt="${mealName}">
                        <p>${data.meal_recipes[mealName]}</p>
                    `;
                    mealsContainer.appendChild(mealDiv);
                });
            } else {
                errorContainer.innerText = data.message || "No meals found";
            }
        } else {
            errorContainer.innerText = data.error || "Failed to fetch meals";
        }
    } catch (error) {
        console.error("Error fetching meals:", error);
        errorContainer.innerText = "An error occurred while fetching meals.";
    }
}
