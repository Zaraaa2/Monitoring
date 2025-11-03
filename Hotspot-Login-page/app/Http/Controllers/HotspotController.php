<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;
use Illuminate\Support\Facades\Hash;

class HotspotController extends Controller
{
    public function index(Request $request)
    {
        // Get Mikrotik parameters (nanti dari redirect)
        $mac = $request->query('mac', 'AA:BB:CC:DD:EE:FF');
        $ip = $request->query('ip', $request->ip());
        $username = $request->query('username', '');
        $linkOrig = $request->query('link-orig', 'http://google.com');
        
        return view('login', compact('mac', 'ip', 'username', 'linkOrig'));
    }

    public function authenticate(Request $request)
    {
        $request->validate([
            'username' => 'required|string',
            'password' => 'required|string',
        ]);

        $username = $request->input('username');
        $password = $request->input('password');
        
        // Development mode: simple authentication
        // TODO: Integrate dengan database dan Mikrotik API
        if ($username === 'admin' && $password === '1234') {
            // Login berhasil
            session(['user_id' => 1]);
            session(['username' => $username]);
            
            return redirect()->route('status')->with('info', 'Development Mode: Login successful');
        }
        
        // Login gagal
        return back()->with('error', 'Invalid username or password');
    }

    public function status()
    {
        if (!session('user_id')) {
            return redirect()->route('login');
        }
        
        return view('status');
    }

    public function logout()
    {
        session()->flush();
        return redirect()->route('login')->with('success', 'Logged out successfully');
    }

    public function error()
    {
        $error = session('error', 'An error occurred');
        return view('error', compact('error'));
    }
}
