$content = Get-Content -Path "index.html" -Raw

$newHero = @"
<div class="relative w-full overflow-hidden bg-slate-50">
    <div id="hero-slider-container" class="flex transition-transform duration-500 ease-in-out w-full">
        <!-- Slide 1 -->
        <div class="hero-slide w-full flex-shrink-0 grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-center py-8 px-8 sm:px-16 min-h-[340px] md:min-h-[380px] lg:min-h-[420px]">
            <div class="space-y-5 text-left max-w-xl">
                <span class="inline-flex items-center gap-2 px-3 py-1 bg-emerald-50 text-emerald-600 text-xs font-bold rounded-lg uppercase tracking-wider">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                    </span>
                    Kategori Pilihan
                </span>
                <h1 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 leading-tight">Lapis Talas Bogor</h1>
                <p class="text-slate-500 text-xs sm:text-sm md:text-base leading-relaxed line-clamp-3">Bolu Lapis talas khas Bogor yang lembut dan tekstur yang rapat tapi tetap lembut dengan varian rasa baru</p>
                <div class="pt-2">
                    <a href="store.html?category=Lapis%20Talas%20Bogor" class="inline-flex items-center gap-2 px-6 py-3 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold shadow-lg shadow-emerald-600/10 transition-all transform hover:-translate-y-0.5">
                        Lihat Koleksi <i class="bi bi-arrow-right"></i>
                    </a>
                </div>
            </div>
            <div class="hidden md:flex relative group justify-center md:justify-end items-center p-4">
                <div class="absolute w-80 h-80 lg:w-[380px] lg:h-[380px] bg-gradient-to-tr from-emerald-500/10 to-transparent rounded-full blur-2xl"></div>
                <div class="relative w-80 h-80 lg:w-[380px] lg:h-[380px] rounded-2xl overflow-hidden border border-slate-100 bg-white shadow-xl shadow-slate-200/50">
                    <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775358042/yuton17knzkrclbeo5pp.jpg" alt="Lapis Talas Bogor" class="w-full h-full object-cover transition-transform duration-700 hover:scale-105">
                </div>
            </div>
        </div>
        <!-- Slide 2 -->
        <div class="hero-slide w-full flex-shrink-0 grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-center py-8 px-8 sm:px-16 min-h-[340px] md:min-h-[380px] lg:min-h-[420px]">
            <div class="space-y-5 text-left max-w-xl">
                <span class="inline-flex items-center gap-2 px-3 py-1 bg-emerald-50 text-emerald-600 text-xs font-bold rounded-lg uppercase tracking-wider">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                    </span>
                    Terlaris
                </span>
                <h1 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 leading-tight">Bolu Susu Madu</h1>
                <p class="text-slate-500 text-xs sm:text-sm md:text-base leading-relaxed line-clamp-3">Bolu susu lembut dengan manis alami madu pilihan yang memberikan sensasi rasa istimewa di setiap gigitan.</p>
                <div class="pt-2">
                    <a href="store.html?category=Bolu%20Susu%20Madu" class="inline-flex items-center gap-2 px-6 py-3 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold shadow-lg shadow-emerald-600/10 transition-all transform hover:-translate-y-0.5">
                        Lihat Koleksi <i class="bi bi-arrow-right"></i>
                    </a>
                </div>
            </div>
            <div class="hidden md:flex relative group justify-center md:justify-end items-center p-4">
                <div class="absolute w-80 h-80 lg:w-[380px] lg:h-[380px] bg-gradient-to-tr from-emerald-500/10 to-transparent rounded-full blur-2xl"></div>
                <div class="relative w-80 h-80 lg:w-[380px] lg:h-[380px] rounded-2xl overflow-hidden border border-slate-100 bg-white shadow-xl shadow-slate-200/50">
                    <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775357468/srqjjk48kvk7vdvwvyrh.jpg" alt="Bolu Susu Madu" class="w-full h-full object-cover transition-transform duration-700 hover:scale-105">
                </div>
            </div>
        </div>
        <!-- Slide 3 -->
        <div class="hero-slide w-full flex-shrink-0 grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-center py-8 px-8 sm:px-16 min-h-[340px] md:min-h-[380px] lg:min-h-[420px]">
            <div class="space-y-5 text-left max-w-xl">
                <span class="inline-flex items-center gap-2 px-3 py-1 bg-emerald-50 text-emerald-600 text-xs font-bold rounded-lg uppercase tracking-wider">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                    </span>
                    Rasa Baru
                </span>
                <h1 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 leading-tight">Pie Susu Lembang</h1>
                <p class="text-slate-500 text-xs sm:text-sm md:text-base leading-relaxed line-clamp-3">Nikmati renyahnya kulit pie berpadu dengan isian susu yang manis dan creamy, cocok untuk teman minum teh.</p>
                <div class="pt-2">
                    <a href="store.html?category=Pie%20Susu" class="inline-flex items-center gap-2 px-6 py-3 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold shadow-lg shadow-emerald-600/10 transition-all transform hover:-translate-y-0.5">
                        Lihat Koleksi <i class="bi bi-arrow-right"></i>
                    </a>
                </div>
            </div>
            <div class="hidden md:flex relative group justify-center md:justify-end items-center p-4">
                <div class="absolute w-80 h-80 lg:w-[380px] lg:h-[380px] bg-gradient-to-tr from-emerald-500/10 to-transparent rounded-full blur-2xl"></div>
                <div class="relative w-80 h-80 lg:w-[380px] lg:h-[380px] rounded-2xl overflow-hidden border border-slate-100 bg-white shadow-xl shadow-slate-200/50">
                    <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775363301/yqy1hjkqhizbb0soq0fy.png" alt="Pie Susu Lembang" class="w-full h-full object-cover transition-transform duration-700 hover:scale-105">
                </div>
            </div>
        </div>
        <!-- Slide 4 -->
        <div class="hero-slide w-full flex-shrink-0 grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-center py-8 px-8 sm:px-16 min-h-[340px] md:min-h-[380px] lg:min-h-[420px]">
            <div class="space-y-5 text-left max-w-xl">
                <span class="inline-flex items-center gap-2 px-3 py-1 bg-emerald-50 text-emerald-600 text-xs font-bold rounded-lg uppercase tracking-wider">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                    </span>
                    Favorit Keluarga
                </span>
                <h1 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 leading-tight">Bakpia Khas Jogja</h1>
                <p class="text-slate-500 text-xs sm:text-sm md:text-base leading-relaxed line-clamp-3">Hadirkan kehangatan keluarga dengan bakpia khas Jogja yang lembut dengan berbagai pilihan isian yang lezat.</p>
                <div class="pt-2">
                    <a href="store.html?category=Bakpia%20Khas%20Jogja" class="inline-flex items-center gap-2 px-6 py-3 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold shadow-lg shadow-emerald-600/10 transition-all transform hover:-translate-y-0.5">
                        Lihat Koleksi <i class="bi bi-arrow-right"></i>
                    </a>
                </div>
            </div>
            <div class="hidden md:flex relative group justify-center md:justify-end items-center p-4">
                <div class="absolute w-80 h-80 lg:w-[380px] lg:h-[380px] bg-gradient-to-tr from-emerald-500/10 to-transparent rounded-full blur-2xl"></div>
                <div class="relative w-80 h-80 lg:w-[380px] lg:h-[380px] rounded-2xl overflow-hidden border border-slate-100 bg-white shadow-xl shadow-slate-200/50">
                    <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775363415/wmgozpn86vtqiau8i1oz.png" alt="Bakpia Khas Jogja" class="w-full h-full object-cover transition-transform duration-700 hover:scale-105">
                </div>
            </div>
        </div>
    </div>
</div>
"@

$newDots = @"
<div id="slider-dots" class="flex justify-center gap-2">
    <button class="slider-dot h-2 w-8 bg-emerald-600 rounded-full transition-all duration-300" data-index="0"></button>
    <button class="slider-dot h-2 w-2 bg-slate-300 hover:bg-slate-400 rounded-full transition-all duration-300" data-index="1"></button>
    <button class="slider-dot h-2 w-2 bg-slate-300 hover:bg-slate-400 rounded-full transition-all duration-300" data-index="2"></button>
    <button class="slider-dot h-2 w-2 bg-slate-300 hover:bg-slate-400 rounded-full transition-all duration-300" data-index="3"></button>
</div>
"@

$newScript = @"
        if (sidebarBackdrop) sidebarBackdrop.addEventListener('click', closeMenu);

        // Hero Slider Logic
        const sliderContainer = document.getElementById('hero-slider-container');
        const sliderDots = document.querySelectorAll('.slider-dot');
        let currentSlide = 0;
        const totalSlides = sliderDots.length;
        let slideInterval;

        function updateSlider(index) {
            currentSlide = index;
            // Update transform
            if(sliderContainer) {
                sliderContainer.style.transform = `translateX(-` + (currentSlide * 100) + `%)`;
            }
            
            // Update dots
            sliderDots.forEach((dot, i) => {
                if (i === currentSlide) {
                    dot.classList.remove('w-2', 'bg-slate-300', 'hover:bg-slate-400');
                    dot.classList.add('w-8', 'bg-emerald-600');
                } else {
                    dot.classList.remove('w-8', 'bg-emerald-600');
                    dot.classList.add('w-2', 'bg-slate-300', 'hover:bg-slate-400');
                }
            });
        }

        function nextSlide() {
            const next = (currentSlide + 1) % totalSlides;
            updateSlider(next);
        }

        function startSlider() {
            slideInterval = setInterval(nextSlide, 5000);
        }

        function stopSlider() {
            clearInterval(slideInterval);
        }

        // Add click events to dots
        sliderDots.forEach(dot => {
            dot.addEventListener('click', (e) => {
                const index = parseInt(e.target.getAttribute('data-index'));
                updateSlider(index);
                stopSlider();
                startSlider(); // Reset interval
            });
        });

        // Pause on hover
        if(sliderContainer) {
            sliderContainer.addEventListener('mouseenter', stopSlider);
            sliderContainer.addEventListener('mouseleave', startSlider);
            // Start slider
            startSlider();
        }
    </script>
"@

$content = $content -replace '(?s)<div id="hero-slider-container".*?</div>\s*</div>\s*</div>\s*</div>', $newHero
$content = $content -replace '(?s)<div id="slider-dots".*?</div>', $newDots
$content = $content -replace '(?s)if \(sidebarBackdrop\) sidebarBackdrop\.addEventListener\(''click'', closeMenu\);\s*</script>', $newScript

Set-Content -Path "index.html" -Value $content -Encoding UTF8
