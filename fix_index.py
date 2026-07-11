import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the top part: from line 152 to 226
# We can find the exact string to replace
top_search = """                <a href="contact.html"
                    class="flex items-center gap-3.5 px-4 py-3 rounded-xl hover:bg-slate-50 hover:text-emerald-600 transition-all">
            </div>
            <div class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Lapis Talas
                    Bogor</p>
            </div>
            </a>
            <a href="store.html?category=Bolu%20Susu%20Madu"
                class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775357468/srqjjk48kvk7vdvwvyrh.jpg"
                    alt="Bolu Susu Madu"
                    class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors">
                </div>
                <div
                    class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                    <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Bolu Susu Madu
                    </p>
                </div>
            </a>
            <a href="store.html?category=Pie%20Susu"
                class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775363301/yqy1hjkqhizbb0soq0fy.png"
                    alt="Pie Susu"
                    class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors">
                </div>
                <div
                    class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                    <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Pie Susu</p>
                </div>
            </a>
            <a href="store.html?category=Bolu%20Susu"
                class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775357049/zdxupjv1qmqbh3btekrx.jpg"
                    alt="Bolu Susu"
                    class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors">
                </div>
                <div
                    class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                    <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Bolu Susu</p>
                </div>
            </a>
            <a href="store.html?category=Bakpia%20Khas%20Jogja"
                class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775363415/wmgozpn86vtqiau8i1oz.png"
                    alt="Bakpia Khas Jogja"
                    class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors">
                </div>
                <div
                    class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                    <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Bakpia Khas
                        Jogja</p>
                </div>
            </a>
            <a href="store.html?category=Tiramisu%20coklat%20Lumer"
                class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775358861/nm7sr2zwwtkviwpt6dhv.jpg"
                    alt="Tiramisu coklat Lumer"
                    class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors">
                </div>
                <div
                    class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                    <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Tiramisu coklat
                        Lumer
                    </p>
                </div>
            </a>
        </div>
    </div>
    </section>"""

top_replace = """                <a href="contact.html"
                    class="flex items-center gap-3.5 px-4 py-3 rounded-xl hover:bg-slate-50 hover:text-emerald-600 transition-all">
                    <i class="bi bi-envelope text-lg"></i>
                    <span>Contact</span>
                </a>
            </div>
            <!-- Drawer Footer CTA -->
            <div class="p-5 border-t border-slate-100 bg-slate-50/80 space-y-3">
                <a href="https://wa.me/6287885038485" target="_blank"
                    class="flex items-center justify-center gap-2 w-full py-3 px-4 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-white font-bold text-sm shadow-md shadow-emerald-500/20 transition-all">
                    <i class="bi bi-whatsapp text-base"></i>
                    <span>Chat WhatsApp</span>
                </a>
                <p class="text-[11px] text-center text-slate-400">© 2026 Geka Store</p>
            </div>
        </div>
    </div>

    <!-- HERO SLIDER -->
    <section class="relative bg-slate-50 pt-24 pb-12 lg:pt-32 lg:pb-20 overflow-hidden">
        <div id="hero-slider-container" class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-[500px] sm:h-[600px] lg:h-[550px] rounded-3xl overflow-hidden shadow-2xl group">
            
            <!-- Slide 1 -->
            <div class="hero-slide absolute inset-0 transition-opacity duration-700 ease-in-out opacity-100 pointer-events-auto z-10">
                <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775357049/zdxupjv1qmqbh3btekrx.jpg" alt="Bolu Susu Lembang" class="absolute inset-0 w-full h-full object-cover">
                <div class="absolute inset-0 bg-gradient-to-r from-slate-900/80 via-slate-900/50 to-transparent"></div>
                <div class="absolute inset-0 flex items-center">
                    <div class="px-8 sm:px-12 lg:px-16 max-w-2xl space-y-4 sm:space-y-6">
                        <span class="inline-block px-3 py-1 bg-emerald-500 text-white text-xs font-bold uppercase tracking-wider rounded-full">Best Seller</span>
                        <h2 class="text-3xl sm:text-5xl lg:text-6xl font-black text-white leading-tight">Bolu Susu Lembang Original</h2>
                        <p class="text-slate-200 text-sm sm:text-base lg:text-lg font-medium max-w-lg">Kelezatan autentik bolu susu dengan kelembutan sempurna dan taburan keju melimpah.</p>
                        <a href="store.html" class="inline-flex items-center gap-2 px-6 py-3 bg-emerald-500 hover:bg-emerald-600 text-white font-bold rounded-xl transition-all shadow-lg shadow-emerald-500/30 hover:-translate-y-1">
                            Pesan Sekarang <i class="bi bi-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Slide 2 -->
            <div class="hero-slide absolute inset-0 transition-opacity duration-700 ease-in-out opacity-0 pointer-events-none z-0">
                <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775358042/yuton17knzkrclbeo5pp.jpg" alt="Lapis Talas Bogor" class="absolute inset-0 w-full h-full object-cover">
                <div class="absolute inset-0 bg-gradient-to-r from-slate-900/80 via-slate-900/50 to-transparent"></div>
                <div class="absolute inset-0 flex items-center">
                    <div class="px-8 sm:px-12 lg:px-16 max-w-2xl space-y-4 sm:space-y-6">
                        <span class="inline-block px-3 py-1 bg-emerald-500 text-white text-xs font-bold uppercase tracking-wider rounded-full">Favorit Baru</span>
                        <h2 class="text-3xl sm:text-5xl lg:text-6xl font-black text-white leading-tight">Lapis Talas Bogor</h2>
                        <p class="text-slate-200 text-sm sm:text-base lg:text-lg font-medium max-w-lg">Perpaduan talas lembut khas Bogor dengan berbagai varian topping premium.</p>
                        <a href="store.html?category=Lapis%20Talas%20Bogor" class="inline-flex items-center gap-2 px-6 py-3 bg-emerald-500 hover:bg-emerald-600 text-white font-bold rounded-xl transition-all shadow-lg shadow-emerald-500/30 hover:-translate-y-1">
                            Lihat Varian <i class="bi bi-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Slide 3 -->
            <div class="hero-slide absolute inset-0 transition-opacity duration-700 ease-in-out opacity-0 pointer-events-none z-0">
                <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775363301/yqy1hjkqhizbb0soq0fy.png" alt="Pie Susu" class="absolute inset-0 w-full h-full object-cover">
                <div class="absolute inset-0 bg-gradient-to-r from-slate-900/80 via-slate-900/50 to-transparent"></div>
                <div class="absolute inset-0 flex items-center">
                    <div class="px-8 sm:px-12 lg:px-16 max-w-2xl space-y-4 sm:space-y-6">
                        <span class="inline-block px-3 py-1 bg-emerald-500 text-white text-xs font-bold uppercase tracking-wider rounded-full">Renyah & Manis</span>
                        <h2 class="text-3xl sm:text-5xl lg:text-6xl font-black text-white leading-tight">Pie Susu Lembang</h2>
                        <p class="text-slate-200 text-sm sm:text-base lg:text-lg font-medium max-w-lg">Pie renyah dengan vla susu lembut yang lumer di mulut. Cocok untuk camilan keluarga.</p>
                        <a href="store.html?category=Pie%20Susu" class="inline-flex items-center gap-2 px-6 py-3 bg-emerald-500 hover:bg-emerald-600 text-white font-bold rounded-xl transition-all shadow-lg shadow-emerald-500/30 hover:-translate-y-1">
                            Beli Sekarang <i class="bi bi-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Navigation Buttons -->
            <button id="hero-prev" class="absolute left-4 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/20 hover:bg-white/40 backdrop-blur-md text-white flex items-center justify-center transition-all opacity-0 group-hover:opacity-100 focus:outline-none z-20">
                <i class="bi bi-chevron-left text-xl"></i>
            </button>
            <button id="hero-next" class="absolute right-4 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/20 hover:bg-white/40 backdrop-blur-md text-white flex items-center justify-center transition-all opacity-0 group-hover:opacity-100 focus:outline-none z-20">
                <i class="bi bi-chevron-right text-xl"></i>
            </button>

            <!-- Dots -->
            <div class="absolute bottom-6 left-1/2 -translate-x-1/2 flex items-center gap-2 z-20">
                <button class="hero-dot h-2.5 w-9 bg-emerald-600 rounded-full transition-all duration-300 focus:outline-none" aria-label="Slide 1"></button>
                <button class="hero-dot h-2.5 w-2.5 bg-slate-300/50 hover:bg-slate-300 rounded-full transition-all duration-300 focus:outline-none" aria-label="Slide 2"></button>
                <button class="hero-dot h-2.5 w-2.5 bg-slate-300/50 hover:bg-slate-300 rounded-full transition-all duration-300 focus:outline-none" aria-label="Slide 3"></button>
            </div>
        </div>
    </section>

    <!-- CATEGORIES SECTION -->
    <section class="py-12 bg-white relative z-20 -mt-8">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
                <a href="store.html?category=Lapis%20Talas%20Bogor" class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                    <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775358042/yuton17knzkrclbeo5pp.jpg" alt="Lapis Talas Bogor" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                    <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors"></div>
                    <div class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                        <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Lapis Talas Bogor</p>
                    </div>
                </a>
                <a href="store.html?category=Bolu%20Susu%20Madu" class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                    <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775357468/srqjjk48kvk7vdvwvyrh.jpg" alt="Bolu Susu Madu" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                    <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors"></div>
                    <div class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                        <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Bolu Susu Madu</p>
                    </div>
                </a>
                <a href="store.html?category=Pie%20Susu" class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                    <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775363301/yqy1hjkqhizbb0soq0fy.png" alt="Pie Susu" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                    <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors"></div>
                    <div class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                        <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Pie Susu</p>
                    </div>
                </a>
                <a href="store.html?category=Bolu%20Susu" class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                    <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775357049/zdxupjv1qmqbh3btekrx.jpg" alt="Bolu Susu" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                    <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors"></div>
                    <div class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                        <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Bolu Susu</p>
                    </div>
                </a>
                <a href="store.html?category=Bakpia%20Khas%20Jogja" class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                    <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775363415/wmgozpn86vtqiau8i1oz.png" alt="Bakpia Khas Jogja" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                    <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors"></div>
                    <div class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                        <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Bakpia Khas Jogja</p>
                    </div>
                </a>
                <a href="store.html?category=Tiramisu%20coklat%20Lumer" class="relative group h-28 rounded-2xl overflow-hidden border border-slate-100 flex items-center justify-center shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
                    <img src="https://res.cloudinary.com/dtqrp1ydo/image/upload/v1775358861/nm7sr2zwwtkviwpt6dhv.jpg" alt="Tiramisu coklat Lumer" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110">
                    <div class="absolute inset-0 bg-slate-900/40 group-hover:bg-slate-900/50 transition-colors"></div>
                    <div class="relative z-10 glass-card px-3 py-2 rounded-xl text-center max-w-[85%] border border-white/20">
                        <p class="text-xs font-black text-slate-900 tracking-tight line-clamp-1">Tiramisu coklat Lumer</p>
                    </div>
                </a>
            </div>
        </div>
    </section>"""

if top_search in content:
    content = content.replace(top_search, top_replace)
else:
    print("Top search string not found!")

first_footer_idx = content.find('    <!-- FOOTER -->\\n    <footer class="bg-slate-900 text-slate-400 pt-16 pb-8 border-t border-slate-800">')
second_footer_idx = content.find('        <!-- FOOTER -->\\n        <footer class="bg-slate-900 text-slate-400 pt-16 pb-8 border-t border-slate-800">')

if first_footer_idx != -1 and second_footer_idx != -1:
    script_idx = content.find('        <!-- SCRIPT -->\\n        <script>')
    if script_idx != -1:
        script_content = content[script_idx:]
        script_content = script_content.replace('        <!-- SCRIPT -->', '    <!-- SCRIPT -->')
        script_content = script_content.replace('        <script>', '    <script>')
        
        correct_footer = """    <!-- FOOTER -->
    <footer class="bg-slate-900 text-slate-400 pt-16 pb-8 border-t border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
            <div class="space-y-4">
                <img src="./asset/logo.png" alt="Logo Footer" class="h-10 w-auto brightness-0 invert">
                <p class="text-sm leading-relaxed text-slate-400">Kami menyediakan solusi digital terbaik untuk membantu
                    bisnis dan UMKM berkembang lebih cepat di era digital modern saat ini.</p>
            </div>
            <div>
                <h4 class="text-white font-semibold text-sm tracking-wider uppercase mb-4">Informasi</h4>
                <ul class="space-y-2.5 text-sm">
                    <li><a href="about.html" class="hover:text-white transition-colors">Tentang Kami</a></li>
                    <li><a href="store.html" class="hover:text-white transition-colors">Toko</a></li>
                    <li><a href="news.html" class="hover:text-white transition-colors">Artikel</a></li>
                    <li><a href="contact.html" class="hover:text-white transition-colors">Kontak</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-semibold text-sm tracking-wider uppercase mb-4">Layanan & Kategori</h4>
                <ul class="space-y-2.5 text-sm">
                    <li><a href="store.html?category=Lapis%20Talas%20Bogor" class="hover:text-white transition-colors">Lapis Talas Bogor</a></li>
                    <li><a href="store.html?category=Bolu%20Susu%20Madu" class="hover:text-white transition-colors">Bolu Susu Madu</a></li>
                    <li><a href="store.html?category=Pie%20Susu" class="hover:text-white transition-colors">Pie Susu Lembang</a></li>
                    <li><a href="store.html?category=Bakpia%20Khas%20Jogja" class="hover:text-white transition-colors">Bakpia Khas Jogja</a></li>
                </ul>
            </div>
            <div class="space-y-4">
                <h4 class="text-white font-semibold text-sm tracking-wider uppercase mb-3">Get In Touch</h4>
                <ul class="space-y-2.5 text-sm">
                    <li class="flex items-start gap-3">
                        <i class="bi bi-geo-alt text-emerald-500 mt-0.5"></i>
                        <span>Jl. Jalur Utama No. 123, Tangerang, Banten</span>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="bi bi-whatsapp text-emerald-500"></i>
                        <a href="https://wa.me/6287885038485" target="_blank" class="hover:text-white transition-colors">+62 878-8503-8485</a>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="bi bi-envelope text-emerald-500"></i>
                        <a href="mailto:info@perusahaan.com" class="hover:text-white transition-colors">info@perusahaan.com</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 border-t border-slate-800 text-sm text-center md:text-left flex flex-col md:flex-row justify-between gap-4">
            <p>© 2026 Geka Store. All rights reserved.</p>
            <p class="text-xs text-slate-500">Designed with Plus Jakarta Sans & Tailwind</p>
        </div>
    </footer>

    <!-- FLOATING WA BUTTON -->
    <a href="https://wa.me/6287885038485" target="_blank"
        class="fixed bottom-6 right-6 z-50 flex items-center justify-center w-14 h-14 bg-emerald-500 text-white rounded-full shadow-lg hover:bg-emerald-600 transition-all duration-300 group hover:scale-110"
        aria-label="Chat via WhatsApp">
        <span class="absolute inset-0 rounded-full bg-emerald-500/40 animate-ping group-hover:animate-none"></span>
        <i class="bi bi-whatsapp text-2xl relative z-10"></i>
    </a>

"""
        content = content[:first_footer_idx] + correct_footer + script_content
    else:
        print("Script section not found!")
else:
    print("Footers not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done fixing index.html")
