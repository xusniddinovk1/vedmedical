// News Portal JavaScript Functionality

// DOM Elements
const mobileMenu = document.getElementById('mobile-menu');
const navMenu = document.querySelector('.nav-menu');
const filterButtons = document.querySelectorAll('.filter-btn');
const newsGrid = document.getElementById('newsGrid');
const searchInput = document.getElementById('searchInput');
const loadMoreBtn = document.getElementById('loadMoreBtn');
const shareButtons = document.querySelectorAll('.share-btn');
const copyLinkBtn = document.getElementById('copyLinkBtn');

// Sample news data for dynamic loading
const newsData = [
    {
        id: 7,
        title: "Space Exploration: New Mission to Mars Announced",
        excerpt: "NASA announces its most ambitious Mars mission yet, featuring advanced robotics and potential human crew preparations...",
        category: "technology",
        date: "March 9, 2024",
        author: "Dr. Space Explorer",
        image: "https://via.placeholder.com/400x250/9c27b0/ffffff?text=Space+Mission"
    },
    {
        id: 8,
        title: "Global Economy Shows Signs of Recovery",
        excerpt: "Economic indicators suggest a strong recovery across major markets, with employment rates reaching pre-pandemic levels...",
        category: "business",
        date: "March 8, 2024",
        author: "Economic Analyst",
        image: "https://via.placeholder.com/400x250/2196f3/ffffff?text=Economy"
    },
    {
        id: 9,
        title: "Environmental Summit Reaches Historic Agreement",
        excerpt: "World leaders unite on comprehensive climate action plan with unprecedented funding commitments...",
        category: "politics",
        date: "March 7, 2024",
        author: "Environmental Reporter",
        image: "https://via.placeholder.com/400x250/4caf50/ffffff?text=Environment"
    }
];

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initMobileMenu();
    initCategoryFilter();
    initSearch();
    initLoadMore();
    initSocialShare();
    initSmoothScroll();
    initNewsletterForm();
    initCommentForm();
    initArticleSpecific();

    // Add loading animations
    addLoadingAnimations();
});

// Mobile Menu Functionality
function initMobileMenu() {
    if (mobileMenu && navMenu) {
        mobileMenu.addEventListener('click', function() {
            navMenu.classList.toggle('active');

            // Animate hamburger menu
            const bars = mobileMenu.querySelectorAll('.bar');
            bars.forEach((bar, index) => {
                bar.style.transform = navMenu.classList.contains('active')
                    ? `rotate(${index === 1 ? '0' : index === 0 ? '45' : '-45'}deg) translate(${index === 0 ? '6px, 6px' : index === 2 ? '6px, -6px' : '0, 0'})`
                    : 'none';
            });
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!mobileMenu.contains(e.target) && !navMenu.contains(e.target)) {
                navMenu.classList.remove('active');
                const bars = mobileMenu.querySelectorAll('.bar');
                bars.forEach(bar => bar.style.transform = 'none');
            }
        });
    }
}

// Category Filter Functionality
function initCategoryFilter() {
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Filter news cards
            const category = this.dataset.category;
            filterNews(category);
        });
    });
}

function filterNews(category) {
    const newsCards = document.querySelectorAll('.news-card');

    newsCards.forEach(card => {
        const cardCategory = card.dataset.category;
        const shouldShow = category === 'all' || cardCategory === category;

        if (shouldShow) {
            card.style.display = 'block';
            card.style.animation = 'fadeInUp 0.6s ease forwards';
        } else {
            card.style.display = 'none';
        }
    });

    // Update results count
    updateResultsCount();
}

// Search Functionality
function initSearch() {
    if (searchInput) {
        searchInput.addEventListener('input', debounce(performSearch, 300));

        const searchBtn = document.querySelector('.search-btn');
        if (searchBtn) {
            searchBtn.addEventListener('click', performSearch);
        }
    }
}

function performSearch() {
    const query = searchInput.value.toLowerCase().trim();
    const newsCards = document.querySelectorAll('.news-card');

    newsCards.forEach(card => {
        const title = card.querySelector('.news-title a').textContent.toLowerCase();
        const excerpt = card.querySelector('.news-excerpt').textContent.toLowerCase();
        const category = card.dataset.category.toLowerCase();

        const matches = title.includes(query) || excerpt.includes(query) || category.includes(query);

        if (query === '' || matches) {
            card.style.display = 'block';
            highlightSearchTerms(card, query);
        } else {
            card.style.display = 'none';
        }
    });

    updateResultsCount();
}

function highlightSearchTerms(card, query) {
    if (!query) return;

    const title = card.querySelector('.news-title a');
    const excerpt = card.querySelector('.news-excerpt');

    [title, excerpt].forEach(element => {
        const text = element.textContent;
        const highlightedText = text.replace(
            new RegExp(`(${query})`, 'gi'),
            '<mark>$1</mark>'
        );
        element.innerHTML = highlightedText;
    });
}

// Load More Functionality
function initLoadMore() {
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', loadMoreNews);
    }
}

function loadMoreNews() {
    // Show loading state
    loadMoreBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
    loadMoreBtn.disabled = true;

    // Simulate API call delay
    setTimeout(() => {
        const newNewsItems = generateNewsItems(newsData);
        newsGrid.insertAdjacentHTML('beforeend', newNewsItems);

        // Reset button
        loadMoreBtn.innerHTML = '<i class="fas fa-plus"></i> Load More News';
        loadMoreBtn.disabled = false;

        // Re-initialize animations for new items
        addLoadingAnimations();

        // Smooth scroll to new content
        const newCards = newsGrid.querySelectorAll('.news-card:nth-last-child(-n+3)');
        if (newCards.length > 0) {
            newCards[0].scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    }, 1000);
}

function generateNewsItems(data) {
    return data.map(item => `
        <article class="news-card" data-category="${item.category}">
            <div class="news-image">
                <img src="${item.image}" alt="${item.title}">
                <div class="category-badge ${item.category}">${item.category.charAt(0).toUpperCase() + item.category.slice(1)}</div>
            </div>
            <div class="news-content">
                <div class="news-meta">
                    <span class="date"><i class="far fa-calendar"></i> ${item.date}</span>
                    <span class="author"><i class="far fa-user"></i> ${item.author}</span>
                </div>
                <h3 class="news-title">
                    <a href="news_detail.html?id=${item.id}">${item.title}</a>
                </h3>
                <p class="news-excerpt">${item.excerpt}</p>
                <div class="news-footer">
                    <a href="news_detail.html?id=${item.id}" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
                    <div class="social-share">
                        <button class="share-btn" data-platform="facebook"><i class="fab fa-facebook"></i></button>
                        <button class="share-btn" data-platform="twitter"><i class="fab fa-twitter"></i></button>
                        <button class="share-btn" data-platform="linkedin"><i class="fab fa-linkedin"></i></button>
                    </div>
                </div>
            </div>
        </article>
    `).join('');
}

// Social Share Functionality
function initSocialShare() {
    document.addEventListener('click', function(e) {
        if (e.target.closest('.share-btn')) {
            const btn = e.target.closest('.share-btn');
            const platform = btn.dataset.platform;
            const url = window.location.href;
            const title = document.title;

            shareToSocialMedia(platform, url, title);
        }
    });

    // Copy link functionality
    if (copyLinkBtn) {
        copyLinkBtn.addEventListener('click', copyCurrentLink);
    }
}

function shareToSocialMedia(platform, url, title) {
    const encodedUrl = encodeURIComponent(url);
    const encodedTitle = encodeURIComponent(title);
    let shareUrl;

    switch (platform) {
        case 'facebook':
            shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodedUrl}`;
            break;
        case 'twitter':
            shareUrl = `https://twitter.com/intent/tweet?url=${encodedUrl}&text=${encodedTitle}`;
            break;
        case 'linkedin':
            shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodedUrl}`;
            break;
        case 'whatsapp':
            shareUrl = `https://wa.me/?text=${encodedTitle} ${encodedUrl}`;
            break;
        default:
            return;
    }

    window.open(shareUrl, '_blank', 'width=600,height=400');
}

function copyCurrentLink() {
    navigator.clipboard.writeText(window.location.href).then(() => {
        showNotification('Link copied to clipboard!', 'success');
    }).catch(() => {
        showNotification('Failed to copy link', 'error');
    });
}

// Smooth Scroll for Anchor Links
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
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
}

// Newsletter Form
function initNewsletterForm() {
    const newsletterForms = document.querySelectorAll('.newsletter-form');

    newsletterForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;

            if (validateEmail(email)) {
                // Simulate subscription
                showNotification('Thank you for subscribing!', 'success');
                this.reset();
            } else {
                showNotification('Please enter a valid email address', 'error');
            }
        });
    });
}

// Comment Form
function initCommentForm() {
    const commentForm = document.querySelector('.comment-form form');

    if (commentForm) {
        commentForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(this);
            const name = this.querySelector('input[type="text"]').value;
            const email = this.querySelector('input[type="email"]').value;
            const comment = this.querySelector('textarea').value;

            if (name && email && comment && validateEmail(email)) {
                addNewComment(name, comment);
                this.reset();
                showNotification('Comment posted successfully!', 'success');
            } else {
                showNotification('Please fill in all fields correctly', 'error');
            }
        });
    }

    // Like buttons
    document.addEventListener('click', function(e) {
        if (e.target.closest('.like-btn')) {
            const btn = e.target.closest('.like-btn');
            const count = parseInt(btn.textContent.match(/\d+/)[0]);
            btn.innerHTML = `<i class="far fa-thumbs-up"></i> ${count + 1}`;
            btn.style.color = '#2563eb';
        }
    });
}

function addNewComment(name, comment) {
    const commentsList = document.querySelector('.comments-list');
    const newComment = document.createElement('div');
    newComment.className = 'comment';
    newComment.innerHTML = `
        <div class="comment-avatar">
            <img src="https://via.placeholder.com/50x50/666/ffffff?text=${name.charAt(0).toUpperCase()}" alt="Avatar">
        </div>
        <div class="comment-content">
            <div class="comment-header">
                <h5>${name}</h5>
                <span class="comment-date">Just now</span>
            </div>
            <p>${comment}</p>
            <div class="comment-actions">
                <button class="like-btn"><i class="far fa-thumbs-up"></i> 0</button>
                <button class="reply-btn">Reply</button>
            </div>
        </div>
    `;

    commentsList.insertBefore(newComment, commentsList.firstChild);

    // Update comment count
    const commentCount = document.getElementById('commentCount');
    if (commentCount) {
        commentCount.textContent = parseInt(commentCount.textContent) + 1;
    }

    // Animate new comment
    newComment.style.opacity = '0';
    newComment.style.transform = 'translateY(-20px)';
    setTimeout(() => {
        newComment.style.transition = 'all 0.3s ease';
        newComment.style.opacity = '1';
        newComment.style.transform = 'translateY(0)';
    }, 100);
}

// Article-specific functionality
function initArticleSpecific() {
    // If we're on an article page, load article data based on URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const articleId = urlParams.get('id');

    if (articleId && window.location.pathname.includes('news_detail.html')) {
        loadArticleData(articleId);
    }

    // Progress reading indicator
    addReadingProgress();
}

function loadArticleData(articleId) {
    // Sample article data (in a real app, this would come from an API)
    const articles = {
        '1': {
            title: 'Breakthrough in Artificial Intelligence: New AI Model Achieves Human-Level Performance',
            category: 'technology',
            date: 'March 15, 2024',
            author: 'John Doe',
            image: 'https://via.placeholder.com/800x400/4285f4/ffffff?text=AI+Technology+Breakthrough'
        },
        '2': {
            title: 'World Cup 2024: Spectacular Opening Ceremony Kicks Off Tournament',
            category: 'sports',
            date: 'March 14, 2024',
            author: 'Jane Smith',
            image: 'https://via.placeholder.com/800x400/34a853/ffffff?text=World+Cup+2024'
        },
        // Add more articles as needed
    };

    const article = articles[articleId];
    if (article) {
        // Update page elements with article data
        const elements = {
            'articleTitle': article.title,
            'articleCategory': article.category,
            'articleDate': article.date,
            'articleAuthor': article.author,
            'breadcrumbCategory': article.category
        };

        Object.entries(elements).forEach(([id, value]) => {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = value;
                if (id === 'articleCategory' || id === 'breadcrumbCategory') {
                    element.className = `category-badge ${article.category}`;
                }
            }
        });

        // Update article image
        const articleImage = document.getElementById('articleImage');
        if (articleImage) {
            articleImage.src = article.image;
            articleImage.alt = article.title;
        }

        // Update page title
        document.title = `${article.title} - NewsPortal`;
    }
}

function addReadingProgress() {
    if (!document.querySelector('.article-body')) return;

    // Create progress bar
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 3px;
        background: #2563eb;
        z-index: 1001;
        transition: width 0.1s ease;
    `;
    document.body.appendChild(progressBar);

    // Update progress on scroll
    window.addEventListener('scroll', () => {
        const article = document.querySelector('.article-body');
        if (!article) return;

        const articleTop = article.offsetTop;
        const articleHeight = article.offsetHeight;
        const windowHeight = window.innerHeight;
        const scrollTop = window.pageYOffset;

        const progress = Math.min(
            100,
            Math.max(0, (scrollTop - articleTop + windowHeight) / articleHeight * 100)
        );

        progressBar.style.width = `${progress}%`;
    });
}

// Utility Functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function updateResultsCount() {
    const visibleCards = document.querySelectorAll('.news-card[style*="block"], .news-card:not([style*="none"])');
    const resultCount = visibleCards.length;

    // You can add a results counter element to display this
    console.log(`Showing ${resultCount} articles`);
}

function addLoadingAnimations() {
    const newsCards = document.querySelectorAll('.news-card');
    newsCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : '#3b82f6'};
        color: white;
        border-radius: 8px;
        z-index: 1002;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 300px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    `;
    notification.textContent = message;

    document.body.appendChild(notification);

    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);

    // Remove after 3 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Keyboard Navigation
document.addEventListener('keydown', function(e) {
    // Escape key closes mobile menu
    if (e.key === 'Escape' && navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
    }

    // Ctrl/Cmd + K for search focus
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        if (searchInput) {
            searchInput.focus();
        }
    }
});

// Lazy Loading for Images
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
}

// Performance monitoring
window.addEventListener('load', function() {
    // Log page load time
    const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
    console.log(`Page loaded in ${loadTime}ms`);
});

// Export functions for potential external use
window.NewsPortal = {
    filterNews,
    performSearch,
    shareToSocialMedia,
    showNotification
};