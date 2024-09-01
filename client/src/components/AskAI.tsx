'use client'
import { useEffect, useState } from "react"
import { SheetSide } from "@/components/SheetSide"
import { useAIModal } from "@/hooks/useAIModal"
import { Button } from "@/components/ui/button"
import { BrainCircuit } from "lucide-react"

export const AskAI = () => {
    const [isMounted, setIsMounted] = useState(false)
    const aiModal = useAIModal()

    useEffect(() => {
        setIsMounted(true)
    }, [])

    if (!isMounted) {
        return null
    }

    return (
        <div className="absolute left-5 bottom-5">
            {!aiModal.isOpen &&  
            <Button className="dark:text-blue-900 dark:hover:bg-blue-200  hover:bg-blue-900 focus:outline-none" onClick={() => aiModal.onOpen()}>
                <BrainCircuit size={'20'}/>
                Ask AI
            </Button>}
            <SheetSide isOpen={aiModal.isOpen} onClose={aiModal.onClose} side="bottom" trigger="Ask AI" description="" title="" className=" h-[550px] w-fit  border-0 ">
                <iframe src="http://localhost:8501" width="600" height='500' className="p-lg"></iframe>
            </SheetSide>
        </div>
    )
}

