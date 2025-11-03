// Alpine.js Component untuk Login Form
function loginForm() {
    return {
        // Data
        username: '',
        password: '',
        loading: false,
        error: '',
        
        // Method: Handle form submit
        async handleSubmit() {
            // Reset error
            this.error = '';
            
            // Validasi
            if (!this.validateForm()) {
                return;
            }
            
            // Set loading state
            this.loading = true;
            
            try {
                // Simulasi delay (hapus ini nanti di production)
                await this.simulateLogin();
                
                // NANTI: Submit ke Mikrotik
                // this.submitToMikrotik();
                
            } catch (e) {
                this.error = 'Login gagal. Silakan coba lagi.';
            } finally {
                this.loading = false;
            }
        },
        
        // Method: Validasi form
        validateForm() {
            if (this.username.length < 3) {
                this.error = 'Username minimal 3 karakter';
                return false;
            }
            
            if (this.password.length < 4) {
                this.error = 'Password minimal 4 karakter';
                return false;
            }
            
            return true;
        },
        
        // Method: Simulasi login (untuk testing)
        simulateLogin() {
            return new Promise((resolve, reject) => {
                setTimeout(() => {
                    // Simulasi: username "admin" password "1234" berhasil
                    if (this.username === 'admin' && this.password === '1234') {
                        alert('Login berhasil!');
                        resolve();
                    } else {
                        this.error = 'Username atau password salah';
                        reject();
                    }
                }, 1500); // Delay 1.5 detik
            });
        },
        
        // NANTI: Method untuk submit ke Mikrotik
        submitToMikrotik() {
            // Form akan submit ke endpoint Mikrotik
            // Mikrotik variables: $(link-login), $(username), $(password)
            
            // Untuk production, form akan POST ke:
            // action="$(link-login)"
            
            console.log('Submitting to Mikrotik...');
        }
    }
}

// Helper: Log ke console
console.log('Hotspot Login System Loaded');