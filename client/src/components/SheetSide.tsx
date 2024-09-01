"use client"
import React from "react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"

const SHEET_SIDES = ["top", "right", "bottom", "left"] as const

type Props = {
  side: typeof SHEET_SIDES[number];
  trigger?: string;
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
  title: string;
  description: string;
  className?: string
}
export function SheetSide({
  side, 
  trigger,
  isOpen,
  onClose,
  title, 
  description, 
  className,  
  children}: Props) {

  const onChange = (open: boolean) => {
    if(!open){
        onClose();
    }
  };

  return (
      <Sheet open={isOpen} onOpenChange={onChange}>
        {/* {trigger }
        <SheetTrigger asChild>
          <Button variant="outline" className="border-0">{trigger}</Button>
        </SheetTrigger> */}
        <SheetContent side={side} className={cn("my-auto mx-auto absolute rounded-md p-10", className)}>
          <SheetHeader>
            <SheetTitle>{title}</SheetTitle>
            <SheetDescription>
              {description}
            </SheetDescription>
          </SheetHeader>
          <div>
              {children}
          </div>
        </SheetContent>
      </Sheet>
  )
}
