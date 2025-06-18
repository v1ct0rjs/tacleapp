"use client"

import { Canvas } from "@react-three/fiber"
import { OrbitControls } from "@react-three/drei"
import { Suspense, useEffect } from "react"

// Un componente de cubo muy simple
function Box(props) {
  return (
    <mesh {...props}>
      <boxGeometry args={[1, 1, 1]} /> {/* Un cubo de 1x1x1 */}
      <meshStandardMaterial color="orange" /> {/* Un material naranja simple */}
    </mesh>
  )
}

export function Stage3d(props) {
  const inheritedStyle = props.style || {}

  useEffect(() => {
    console.log("Stage3d React Component MOUNTED! (3D Cube Test)")
    console.log("Props received by Stage3d (3D Cube Test):", props)
    console.log("props.style received (3D Cube Test):", inheritedStyle)
  }, [props, inheritedStyle])

  // Este div DEBE tener dimensiones para que el Canvas funcione.
  // Reflex debería pasar height="60vh" y width="100%" aquí.
  const wrapperStyle = {
    height: inheritedStyle.height || "400px", // Fallback si no se provee height
    width: inheritedStyle.width || "100%", // Fallback si no se provee width
    border: "2px solid green", // Borde verde para ver claramente el área del div
    backgroundColor: "#e0e0e0", // Fondo gris claro para el div
  }

  console.log("Applying wrapperStyle (3D Cube Test):", wrapperStyle)

  return (
    <div style={wrapperStyle}>
      <Canvas
        frameloop="demand" // Renderiza bajo demanda
        camera={{ position: [2, 2, 3], fov: 50 }} // Posición de cámara para ver el cubo en el origen
      >
        {/* Luces básicas */}
        <ambientLight intensity={0.8} />
        <directionalLight position={[5, 5, 5]} intensity={1} />

        <Suspense fallback={null}>
          <Box position={[0, 0, 0]} /> {/* Coloca el cubo en el origen */}
        </Suspense>

        <OrbitControls enableZoom={true} />
      </Canvas>
    </div>
  )
}
