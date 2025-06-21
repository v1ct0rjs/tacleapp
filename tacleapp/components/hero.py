import reflex as rx


def hero() -> rx.Component:
  """Hero section component."""
  return rx.box(
      # Background effects
      rx.box(
          class_name="absolute inset-0 bg-black"
      ),
      rx.box(
          class_name="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-red-900/25 via-transparent to-transparent opacity-50"
      ),

      # Content
      rx.container(
          rx.flex(
              # Main Logo
              rx.image(
                  src="/logo_header.png",
                  alt="10TACLE Logo",
                  class_name="h-auto w-full max-w-md sm:max-w-lg md:max-w-xl mx-auto mb-6"
              ),

              # Subtitle
              rx.text(
                  "Electronic Music Producer & DJ",
                  size="5",
                  class_name="font-orbitron text-gray-400 tracking-widest uppercase mb-8 text-center",
                  as_="div"
              ),

              # Description
              rx.text(
                  """
                  The purest TECHNO throbs, 
                  strong and sensitive is incorruptible, 
                  brave and unique.
                  The purest TECHNO reject the obscene and detect perversion.
                  The purest TECHNO don't fake love nor feign freedom.
                  TECHNO is you and me.
                  """,
                  size="3",
                  class_name="text-gray-300 mb-12 max-w-2xl text-center leading-relaxed",
                  style={"white_space": "pre-wrap"},
                  as_="div"
              ),

              # Buttons
              rx.flex(
                  rx.button(
                      rx.icon("play", size=20, class_name="mr-2"),
                      "Listen Now",
                      size="3",
                      class_name="bg-red-500 hover:bg-red-600 text-white font-bold border-0 px-8 py-6 tracking-wider"
                  ),
                  rx.button(
                      "View Events",
                      size="3",
                      variant="outline",
                      class_name="border-gray-500 text-gray-300 hover:bg-white hover:text-black font-bold px-8 py-6 tracking-wider bg-transparent"
                  ),
                  spacing="4",
                  class_name="flex-col sm:flex-row"
              ),

              direction="column",
              align="center",
              class_name="text-center"
          ),
          class_name="relative z-10 max-w-4xl mx-auto px-4"
      ),

      id="home",
      class_name="relative min-h-screen flex items-center justify-center overflow-hidden pt-20"
  )
