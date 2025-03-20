document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const cityInput = document.getElementById('cityInput');
    const searchBtn = document.getElementById('searchBtn');
    const weatherCard = document.getElementById('weatherCard');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const errorMessage = document.getElementById('errorMessage');
    const loginBtn = document.getElementById('loginBtn');
    const loginModal = document.getElementById('loginModal');
    const loginForm = document.getElementById('loginForm');
    const mobileMenuBtn = document.querySelector('.mobile-menu');
    const navLinks = document.querySelector('.nav-links');
    const unitToggleButtons = document.querySelectorAll('.unit-toggle button');

    // API Configuration
    const API_URL = 'http://localhost:5000/api/v1';
    let currentUnit = 'metric';

    // Weather Icons Mapping
    const weatherIcons = {
        'clear sky': 'sun',
        'few clouds': 'cloud-sun',
        'scattered clouds': 'cloud',
        'broken clouds': 'cloud',
        'shower rain': 'cloud-showers-heavy',
        'rain': 'cloud-rain',
        'thunderstorm': 'bolt',
        'snow': 'snowflake',
        'mist': 'smog',
        'default': 'cloud'
    };

    // Weather API Functions
    async function getWeather(city) {
        try {
            showLoading();
            hideError();

            const response = await fetch(
                `${API_URL}/weather?city=${encodeURIComponent(city)}&units=${currentUnit}`
            );
            const data = await response.json();

            if (data.status === 'success') {
                updateWeatherUI(data.data);
                saveToHistory(data.data);
            } else {
                throw new Error(data.error || 'Failed to fetch weather data');
            }
        } catch (error) {
            showError(error.message);
        } finally {
            hideLoading();
        }
    }

    function updateWeatherUI(weather) {
        // Update location info
        weatherCard.querySelector('.city').textContent = weather.city_name;
        weatherCard.querySelector('.country').textContent = weather.country;

        // Update temperature with animation
        const tempElement = weatherCard.querySelector('.temp');
        animateTemperature(tempElement, parseFloat(weather.temperature));
        weatherCard.querySelector('.description').textContent = weather.description;

        // Update weather icon
        const iconElement = weatherCard.querySelector('.temp-icon i');
        iconElement.className = `fas ${getWeatherIcon(weather.description)}`;

        // Update details
        weatherCard.querySelector('.feels-like').textContent = weather.feels_like;
        weatherCard.querySelector('.humidity').textContent = weather.humidity;
        weatherCard.querySelector('.wind-speed').textContent = weather.wind_speed;
        weatherCard.querySelector('.pressure').textContent = `${weather.pressure} hPa`;

        // Update timestamp
        document.getElementById('timestamp').textContent = 
            `Updated ${new Date().toLocaleTimeString()}`;

        // Show weather card with animation
        weatherCard.style.display = 'block';
        weatherCard.style.opacity = '0';
        requestAnimationFrame(() => {
            weatherCard.style.opacity = '1';
        });
    }

    // UI Helper Functions
    function getWeatherIcon(condition) {
        const normalizedCondition = condition.toLowerCase();
        return `fa-${weatherIcons[normalizedCondition] || weatherIcons.default}`;
    }

    function animateTemperature(element, newValue) {
        const currentValue = parseFloat(element.textContent) || 0;
        const step = (newValue - currentValue) / 50;
        let current = currentValue;

        function update() {
            if (Math.abs(newValue - current) > Math.abs(step)) {
                current += step;
                element.textContent = `${current.toFixed(1)}°${currentUnit === 'metric' ? 'C' : 'F'}`;
                requestAnimationFrame(update);
            } else {
                element.textContent = `${newValue.toFixed(1)}°${currentUnit === 'metric' ? 'C' : 'F'}`;
            }
        }

        requestAnimationFrame(update);
    }

    function showLoading() {
        loadingSpinner.style.display = 'flex';
        weatherCard.style.display = 'none';
    }

    function hideLoading() {
        loadingSpinner.style.display = 'none';
    }

    function showError(message) {
        errorMessage.querySelector('span').textContent = message;
        errorMessage.style.display = 'flex';
        setTimeout(() => {
            errorMessage.style.opacity = '1';
        }, 10);
    }

    function hideError() {
        errorMessage.style.opacity = '0';
        setTimeout(() => {
            errorMessage.style.display = 'none';
        }, 300);
    }

    // History Management
    function saveToHistory(weather) {
        const history = JSON.parse(localStorage.getItem('weatherHistory') || '[]');
        const newEntry = {
            ...weather,
            timestamp: new Date().toISOString()
        };
        history.unshift(newEntry);
        localStorage.setItem('weatherHistory', JSON.stringify(history.slice(0, 5)));
        updateHistoryUI();
    }

    function updateHistoryUI() {
        const historyCards = document.getElementById('historyCards');
        const history = JSON.parse(localStorage.getItem('weatherHistory') || '[]');

        historyCards.innerHTML = history.map(entry => `
            <div class="history-card glass-effect">
                <div class="history-header">
                    <h3>${entry.city_name}, ${entry.country}</h3>
                    <span>${new Date(entry.timestamp).toLocaleString()}</span>
                </div>
                <div class="history-temp">
                    <i class="fas ${getWeatherIcon(entry.description)}"></i>
                    <span>${entry.temperature}</span>
                </div>
            </div>
        `).join('');
    }

    // Event Listeners
    searchBtn.addEventListener('click', () => {
        const city = cityInput.value.trim();
        if (city) getWeather(city);
    });

    cityInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const city = cityInput.value.trim();
            if (city) getWeather(city);
        }
    });

    unitToggleButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (!button.classList.contains('active')) {
                unitToggleButtons.forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');
                currentUnit = button.dataset.unit;
                const city = cityInput.value.trim();
                if (city) getWeather(city);
            }
        });
    });

    mobileMenuBtn.addEventListener('click', () => {
        navLinks.classList.toggle('show');
        mobileMenuBtn.classList.toggle('active');
    });

    // Modal Management
    loginBtn.addEventListener('click', () => {
        loginModal.style.display = 'block';
    });

    document.querySelector('.close').addEventListener('click', () => {
        loginModal.style.display = 'none';
    });

    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        // Add login logic here
        loginModal.style.display = 'none';
    });

    window.addEventListener('click', (e) => {
        if (e.target === loginModal) {
            loginModal.style.display = 'none';
        }
    });

    // Smooth Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href'))?.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Initialize
    updateHistoryUI();
    getWeather('London'); // Load default city
});