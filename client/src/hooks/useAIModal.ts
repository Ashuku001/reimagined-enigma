import {create} from "zustand"

interface useAIProps {
    isOpen: boolean;
    onOpen: () => void;
    onClose: () => void;
}

export const useAIModal = create<useAIProps> ((set) => ({
    isOpen: false,
    onOpen: () => set({isOpen: true}),
    onClose: () => set({isOpen: false})
}))
