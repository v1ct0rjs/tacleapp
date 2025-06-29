import '../assets/styles.css'

export const metadata = {
  title: '10tacle - Electronic Music Producer & DJ',
  description: 'Official website of 10tacle - Electronic music producer, DJ and radio host',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body className="bg-black text-white font-sans">{children}</body>
    </html>
  )