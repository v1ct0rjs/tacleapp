import { Mail, Phone, MapPin, Instagram, Twitter, Youtube, Facebook } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"

export default function Contact() {
  const socialLinks = [
    { icon: Instagram, href: "#", label: "Instagram" },
    { icon: Twitter, href: "#", label: "Twitter" },
    { icon: Facebook, href: "#", label: "Facebook" },
    { icon: Youtube, href: "#", label: "YouTube" },
  ]

  return (
    <section id="contact" className="py-20 bg-black">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">
            Get In <span className="text-red-500">Touch</span>
          </h2>
          <div className="w-24 h-1 bg-red-500 mx-auto mb-8"></div>
          <p className="text-gray-400 text-lg max-w-2xl mx-auto">
            Ready to book a performance or collaborate? Let's create something amazing together.
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-12">
          {/* Contact Form */}
          <div className="bg-gray-900/50 rounded-lg p-8 border border-gray-800">
            <h3 className="text-2xl font-bold text-white mb-6">Send a Message</h3>
            <form className="space-y-6">
              <div className="grid sm:grid-cols-2 gap-4">
                <div>
                  <Input
                    placeholder="Your Name"
                    className="bg-gray-800 border-gray-700 text-white placeholder-gray-400 focus:border-red-500"
                  />
                </div>
                <div>
                  <Input
                    type="email"
                    placeholder="Your Email"
                    className="bg-gray-800 border-gray-700 text-white placeholder-gray-400 focus:border-red-500"
                  />
                </div>
              </div>
              <div>
                <Input
                  placeholder="Subject"
                  className="bg-gray-800 border-gray-700 text-white placeholder-gray-400 focus:border-red-500"
                />
              </div>
              <div>
                <Textarea
                  placeholder="Your Message"
                  rows={6}
                  className="bg-gray-800 border-gray-700 text-white placeholder-gray-400 focus:border-red-500 resize-none"
                />
              </div>
              <Button type="submit" size="lg" className="w-full bg-red-500 hover:bg-red-600 text-white border-0">
                Send Message
              </Button>
            </form>
          </div>

          {/* Contact Info */}
          <div className="space-y-8">
            <div>
              <h3 className="text-2xl font-bold text-white mb-6">Contact Information</h3>
              <div className="space-y-4">
                <div className="flex items-center">
                  <Mail className="w-5 h-5 text-red-500 mr-4" />
                  <span className="text-gray-300">booking@dj10tacle.com</span>
                </div>
                <div className="flex items-center">
                  <Phone className="w-5 h-5 text-red-500 mr-4" />
                  <span className="text-gray-300">+1 (555) 123-4567</span>
                </div>
                <div className="flex items-center">
                  <MapPin className="w-5 h-5 text-red-500 mr-4" />
                  <span className="text-gray-300">Los Angeles, CA</span>
                </div>
              </div>
            </div>

            <div>
              <h4 className="text-xl font-bold text-white mb-4">Follow the Journey</h4>
              <div className="flex space-x-4">
                {socialLinks.map((social, index) => (
                  <a
                    key={index}
                    href={social.href}
                    className="w-12 h-12 bg-gray-800 rounded-lg flex items-center justify-center text-gray-400 hover:text-white hover:bg-red-500 transition-all duration-300"
                    aria-label={social.label}
                  >
                    <social.icon className="w-5 h-5" />
                  </a>
                ))}
              </div>
            </div>

            <div className="bg-gray-900/50 rounded-lg p-6 border border-gray-800">
              <h4 className="text-lg font-bold text-white mb-3">Booking Inquiries</h4>
              <p className="text-gray-400 text-sm mb-4">
                For booking requests, please include event details, date, location, and budget range.
              </p>
              <p className="text-gray-400 text-sm">Response time: 24-48 hours</p>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-20 pt-8 border-t border-gray-800 text-center">
          <p className="text-gray-400">© 2024 DJ 10TACLE. All rights reserved.</p>
        </div>
      </div>
    </section>
  )
}
