<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HotspotController;

Route::get('/', function () {
    return redirect('/login');
});

Route::get('/login', [HotspotController::class, 'index'])->name('login');
Route::post('/login', [HotspotController::class, 'authenticate'])->name('login.submit');
Route::get('/status', [HotspotController::class, 'status'])->name('status');
Route::get('/logout', [HotspotController::class, 'logout'])->name('logout');
Route::get('/error', [HotspotController::class, 'error'])->name('error');
