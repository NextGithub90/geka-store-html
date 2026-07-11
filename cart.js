/* =============================================
   GEKA STORE — cart.js (Cart Logic)
   ============================================= */

const CART_STORAGE_KEY = 'geka_store_cart';

// Get cart from localStorage
function getCart() {
    const cart = localStorage.getItem(CART_STORAGE_KEY);
    return cart ? JSON.parse(cart) : [];
}

// Save cart to localStorage
function saveCart(cart) {
    localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(cart));
    updateCartBadge();
}

// Add item to cart
function addToCart(product, quantity = 1, variant = null) {
    const cart = getCart();

    // Create a unique ID based on product ID and variant
    const cartItemId = variant ? `${product.id}-${variant}` : product.id;

    const existingItem = cart.find(item => item.cartItemId === cartItemId);

    if (existingItem) {
        existingItem.quantity += quantity;
    } else {
        cart.push({
            cartItemId: cartItemId,
            productId: product.id,
            name: product.name,
            price: product.price,
            image: product.images ? product.images[0] : (product.image || ''),
            variant: variant,
            quantity: quantity,
            category: product.category
        });
    }

    saveCart(cart);

    // Optional: Show a toast notification here
    showToast(`Berhasil menambahkan ${product.name} ke keranjang!`);
}

// Remove item from cart
function removeFromCart(cartItemId) {
    let cart = getCart();
    cart = cart.filter(item => item.cartItemId !== cartItemId);
    saveCart(cart);
}

// Update item quantity
function updateQuantity(cartItemId, newQuantity) {
    if (newQuantity < 1) return;
    const cart = getCart();
    const item = cart.find(item => item.cartItemId === cartItemId);
    if (item) {
        item.quantity = newQuantity;
        saveCart(cart);
    }
}

// Update cart badge in navbar
function updateCartBadge() {
    const cart = getCart();
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);

    // Update all elements with the cart badge class/id
    const badges = document.querySelectorAll('.cart-badge');
    badges.forEach(badge => {
        badge.textContent = totalItems;
        if (totalItems > 0) {
            badge.classList.remove('hidden');
            badge.classList.add('flex');
        } else {
            // Keep it visible but show 0, or hide it. Let's show 0 for consistency with current design.
            badge.textContent = '0';
        }
    });
}

// Simple Toast Notification
function showToast(message) {
    // Check if toast container exists, if not create it
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.className = 'fixed bottom-24 right-6 z-[110] flex flex-col gap-2 pointer-events-none';
        document.body.appendChild(toastContainer);
    }

    const toast = document.createElement('div');
    toast.className = 'bg-slate-900 text-white px-4 py-3 rounded-xl shadow-xl text-sm font-medium flex items-center gap-3 transform transition-all duration-300 translate-y-10 opacity-0';
    toast.innerHTML = `<i class="bi bi-check-circle-fill text-slate-600 text-lg"></i> <span>${message}</span>`;

    toastContainer.appendChild(toast);

    // Animate in
    setTimeout(() => {
        toast.classList.remove('translate-y-10', 'opacity-0');
    }, 10);

    // Animate out and remove
    setTimeout(() => {
        toast.classList.add('translate-y-10', 'opacity-0');
        setTimeout(() => {
            toast.remove();
        }, 300);
    }, 3000);
}

// Initialize badge on page load
document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();
});
