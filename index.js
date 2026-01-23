// Products Data
const products = [
    {
        id: 1,
        name: "Wireless Headphones",
        description: "Premium sound quality with noise cancellation",
        price: "$199",
        icon: "🎧"
    },
    {
        id: 2,
        name: "Smart Watch",
        description: "Track your fitness and stay connected",
        price: "$299",
        icon: "⌚"
    },
    {
        id: 3,
        name: "Laptop Pro",
        description: "Powerful performance for professionals",
        price: "$1299",
        icon: "💻"
    },
    {
        id: 4,
        name: "Smartphone X",
        description: "Latest flagship with amazing camera",
        price: "$899",
        icon: "📱"
    },
    {
        id: 5,
        name: "Tablet Plus",
        description: "Perfect for work and entertainment",
        price: "$599",
        icon: "📱"
    },
    {
        id: 6,
        name: "Gaming Console",
        description: "Next-gen gaming experience",
        price: "$499",
        icon: "🎮"
    }
];

// Cart Counter
let cartCount = 0;

// Load Products
function loadProducts() {
    const productGrid = document.getElementById('productGrid');
    
    products.forEach(product => {
        const productCard = document.createElement('div');
        productCard.className = 'product-card';
        productCard.innerHTML = `
            <div class="product-image">${product.icon}</div>
            <div class="product-info">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <div class="product-price">${product.price}</div>
                <button class="add-to-cart" onclick="addToCart(${product.id})">
                    Add to Cart
                </button>
            </div>
        `;
        productGrid.appendChild(productCard);
    });
}

// Add to Cart Function
function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    cartCount++;
    document.getElementById('cart-count').textContent = cartCount;
    
    // Show notification
    alert(`${product.name} added to cart! 🛒`);
}

// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Contact Form Submission
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    
    alert(`Thank you ${name}! We'll get back to you soon.\n\nEmail: ${email}\nMessage: ${message}`);
    
    // Reset form
    this.reset();
});

// Scroll Animation
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe sections
document.querySelectorAll('section').forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(section);
});

// Initialize
window.addEventListener('DOMContentLoaded', function() {
    loadProducts();
});