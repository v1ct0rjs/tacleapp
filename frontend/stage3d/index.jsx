"use client"

import { Suspense } from "react"
import { Canvas } from "@react-three/fiber"
import { OrbitControls, useGLTF, Environment } from "@react-three/drei"
import { Html } from "@react-three/drei" // Import moved to the top

function ModelViewer() {
  // Ruta correcta según la ubicación: assets/models/poly-duck.glb -> /models/poly-duck.glb
  const gltfPath = "/models/duck.glb"
  console.log("Intentando cargar GLTF desde:", gltfPath)

  let scene
  let error = null

  try {
    const gltf = useGLTF(gltfPath)
    scene = gltf.scene
    console.log("GLTF cargado exitosamente:", scene)
  } catch (e) {
    error = e
    console.error("Error al cargar GLTF:", error)
  }

  if (error) {
    return (
      <mesh>
        <boxGeometry args={[1, 1, 1]} />
        <meshStandardMaterial color="red" emissive="red" />
      </mesh>
    ) // Cubo rojo si falla la carga
  }

  return scene ? <primitive object={scene} scale={1} /> : null // Ajusta la escala si es necesario
}

export function Stage3d(props) {
  const inheritedStyle = props.style || {}
  const wrapperStyle = {
    height: inheritedStyle.height || "70vh", // Aumentado un poco
    width: inheritedStyle.width || "100%",
    border: "2px solid green", // Borde para ver el contenedor
    backgroundColor: "#f0f0f0", // Fondo claro para contraste
  }

  console.log("Renderizando Stage3d. Props:", props, "Estilo Wrapper:", wrapperStyle)

  return (
    <div style={wrapperStyle}>
      <Canvas camera={{ position: [0, 2, 5], fov: 50 }}>
        <ambientLight intensity={0.7} />
        <directionalLight position={[5, 5, 5]} intensity={1} />
        <Environment preset="sunset" /> {/* Añade un entorno para mejor iluminación */}
        <Suspense fallback={<LoadingFallback />}>
          <ModelViewer />
        </Suspense>
        <OrbitControls />
      </Canvas>
    </div>
  )
}

function LoadingFallback() {
  console.log("Mostrando Fallback de Suspense (cargando modelo)...")
  return (
    <mesh position={[0, 0, 0]}>
      <boxGeometry args={[0.5, 0.5, 0.5]} />
      <meshStandardMaterial color="blue" wireframe />
      <Html center>
        <p style={{ color: "black" }}>Cargando modelo...</p>
      </Html>
    </mesh>
  )
}
