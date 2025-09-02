"use client"

import { useState } from "react"
import Image from "next/image"
import Link from "next/link"
import { Menu, X } from "lucide-react"

export default function Page() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false)

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen)
  }

  const closeMobileMenu = () => {
    setIsMobileMenuOpen(false)
  }

  const navLinks = [
    { name: "Home", href: "#home" },
    { name: "Music", href: "#music" },
    { name: "Contact", href: "#contact" },
  ]

  const socialButtons = [
    {
      name: "Beatport",
      icon: "/assets/TBG-PrimaryIcon-White.svg",
      href: "https://www.beatport.com/es/artist/10tacle/1121502",
    },
    {
      name: "Spotify",
      icon: "/assets/spotify-white-icon.svg",
      href: "https://open.spotify.com/intl-es/artist/4ycl0vQK5aynXLJeRFpanC",
    },
    { name: "SoundCloud", icon: "/assets/soundcloud-white-icon.svg", href: "https://soundcloud.com/10tacle" },
    { name: "Twitch", icon: "/assets/twitch-white-icon.svg", href: "https://www.twitch.tv/v1ct0rdev" },
  ]

  const heroLines = [
    "The purest TECHNO throbs, strong and sensitive is incorruptible, brave and unique.",
    "The purest TECHNO reject the obscure and detect perversion.",
    "The purest TECHNO don't fake love nor feign freedom.",
    "TECHNO is you and me.",
  ]

  return (
    <div className="futuristic-bg min-h-screen text-white">
      {/* Futuristic Background Effects */}
      <div className="matrix-bg"></div>
      <div className="scan-lines"></div>
      <div className="glitch-bg"></div>
      <div className="digital-noise"></div>

      {/* Floating Particles */}
      <div className="particles">
        {[...Array(9)].map((_, i) => (
          <div key={i} className="particle"></div>
        ))}
      </div>

      {/* Connection Lines */}
      <div className="connection-lines">
        {[...Array(4)].map((_, i) => (
          <div key={i} className="connection-line"></div>
        ))}
      </div>

      {/* Navigation */}
      <nav className="fixed top-0 w-full z-50 bg-black/80 backdrop-blur-md border-b border-gray-800">
        <div className="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16 md:h-20">
            <Link href="#home" onClick={closeMobileMenu}>
              <Image
                src="/tacleapp-develop/assets/logo_header.png"
                alt="10TACLE Logo"
                width={120}
                height={40}
                className="h-8 sm:h-10 w-auto"
              />
            </Link>

            <div className="hidden md:flex items-center space-x-6">
              {navLinks.map((link) => (
                <Link
                  key={link.name}
                  href={link.href}
                  className="text-gray-300 hover:text-white transition-colors duration-300 font-orbitron tracking-wider"
                >
                  {link.name}
                </Link>
              ))}
            </div>

            <button
              onClick={toggleMobileMenu}
              className="md:hidden text-white hover:text-red-500 focus:outline-none bg-transparent border-0 p-2 transition-colors"
              aria-expanded={isMobileMenuOpen}
            >
              {isMobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>

        {/* Mobile Menu */}
        {isMobileMenuOpen && (
          <div className="fixed top-20 left-0 right-0 z-40 md:hidden bg-black/95 backdrop-blur-lg border-b border-gray-700 shadow-xl py-2">
            <div className="flex flex-col w-full">
              {navLinks.map((link) => (
                <Link
                  key={link.name}
                  href={link.href}
                  onClick={closeMobileMenu}
                  className="block w-full px-4 py-4 text-lg text-center text-gray-200 hover:bg-red-500 hover:text-white transition-colors duration-300 font-orbitron"
                >
                  {link.name}
                </Link>
              ))}
            </div>
          </div>
        )}
      </nav>

      {/* Hero Section */}
      <section id="home" className="relative min-h-screen flex items-center justify-center pt-24 pb-12">
        <div className="relative z-10 max-w-5xl mx-auto px-3 sm:px-4 text-center">
          <Image
            src="/tacleapp-develop/assets/logo_header.png"
            alt="10TACLE Logo"
            width={600}
            height={200}
            className="h-auto w-full max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg mx-auto mb-6"
          />

          <div className="font-orbitron text-gray-400 tracking-widest uppercase mb-6 text-center text-sm sm:text-base md:text-xl">
            Electronic Music Producer & DJ
          </div>

          <div className="text-gray-300 mb-8 sm:mb-12 text-center leading-relaxed max-w-full sm:max-w-4xl md:max-w-2xl mx-auto">
            {heroLines.map((line, i) => (
              <p
                key={i}
                className="stanza text-xs sm:text-sm md:text-base mb-2"
                style={{ animationDelay: `${i * 1.5}s` }}
              >
                {line}
              </p>
            ))}
          </div>

          <div className="flex flex-wrap justify-center gap-3 sm:gap-4 mt-4 sm:mt-6">
            {socialButtons.map((button) => (
              <Link
                key={button.name}
                href={button.href}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center border border-gray-600 text-gray-300 hover:bg-red-500 hover:text-white hover:border-red-500 font-semibold tracking-wider px-4 py-2 text-sm sm:px-5 sm:py-2.5 transition-colors duration-300 rounded"
              >
                <Image
                  src={button.icon || "/placeholder.svg"}
                  alt={`${button.name} icon`}
                  width={18}
                  height={18}
                  className="mr-2"
                />
                {button.name}
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Music Section */}
      <section id="music" className="relative py-20 px-4">
        <div className="max-w-6xl mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-orbitron font-bold mb-12 text-white">Music</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="bg-gray-900/50 p-6 rounded-lg backdrop-blur-sm">
              <h3 className="text-xl font-semibold mb-4 text-red-500">Latest Tracks</h3>
              <p className="text-gray-300">Discover the latest TECHNO productions and mixes.</p>
            </div>
            <div className="bg-gray-900/50 p-6 rounded-lg backdrop-blur-sm">
              <h3 className="text-xl font-semibold mb-4 text-red-500">Live Sets</h3>
              <p className="text-gray-300">Experience the energy of live TECHNO performances.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="relative py-20 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-orbitron font-bold mb-12 text-white">Contact</h2>
          <div className="bg-gray-900/50 p-8 rounded-lg backdrop-blur-sm">
            <p className="text-gray-300 mb-6">
              Get in touch for bookings, collaborations, or just to talk about TECHNO.
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              {socialButtons.map((button) => (
                <Link
                  key={button.name}
                  href={button.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-red-500 hover:text-white transition-colors duration-300"
                >
                  {button.name}
                </Link>
              ))}
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
