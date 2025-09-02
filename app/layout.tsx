import type React from "react"
import type { Metadata } from "next"
import { Poppins, Orbitron } from "next/font/google"
import { Analytics } from "@vercel/analytics/next"
import { Suspense } from "react"
import "./globals.css"

const poppins = Poppins({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600"],
  variable: "--font-poppins",
  display: "swap",
})

const orbitron = Orbitron({
  subsets: ["latin"],
  weight: ["700", "900"],
  variable: "--font-orbitron",
  display: "swap",
})

export const metadata: Metadata = {
  title: "10tacle - Electronic Music Producer & DJ",
  description: "Official website of 10tacle - Electronic music producer, DJ and radio host",
  generator: "v0.app",
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en" className={`${poppins.variable} ${orbitron.variable}`}>
      <body className={poppins.className}>
        <Suspense fallback={null}>{children}</Suspense>
        <Analytics />
      </body>
    </html>
  )
}
